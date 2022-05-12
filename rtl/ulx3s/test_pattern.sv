// test_pattern.sv
// Copyright (c) 2022 Daniel Cliche
// SPDX-License-Identifier: MIT

module test_pattern #(
    parameter FB_WIDTH = 128,
    parameter FB_HEIGHT = 128
) (
    input  wire logic                        clk,
    input  wire logic                        reset_i,

    // VRAM write
    input  wire logic                        vram_ack_i,
    output      logic                        vram_sel_o,
    output      logic                        vram_wr_o,
    output      logic  [3:0]                 vram_mask_o,
    output      logic [31:0]                 vram_addr_o,
    output      logic [15:0]                 vram_data_out_o,

    input  wire logic                        fill_i,

    output      logic                        activity_o,

    output      logic [1:0]                  state_o
);

    enum { FILL0, FILL1, FILL2, HOLD } state;

    logic [31:0] addr;
    logic [11:0] line_counter, col_counter;

    logic [11:0] bg_color;
    logic [11:0] color;

    logic [15:0] counter;

    //assign color = line_counter == 0 || line_counter == (FB_HEIGHT - 1) || col_counter == 0 || col_counter == (FB_WIDTH - 1) ? 12'hFFF : {4'hF, addr[0] ? bg_color : 12'h000};
    assign color = {4'hF, addr[0] ? bg_color : 12'h000};

    assign state_o = state;

    always_ff @(posedge clk) begin
        if (reset_i) begin
            addr            <= 24'd0;
            state           <= HOLD;
            vram_sel_o      <= 1'b0;
            vram_mask_o     <= 4'hF;
            vram_wr_o       <= 1'b0;
            vram_data_out_o <= 16'h0;
            line_counter    <= 12'd0;
            col_counter     <= 12'd0;
            bg_color        <= 12'h00F;
            activity_o      <= 1'b0;
        end else begin
            case (state)
                FILL0: begin
                    if (col_counter >= FB_WIDTH) begin
                        col_counter <= 0;
                        line_counter <= line_counter + 1;
                    end else begin
                        col_counter <= col_counter + 1;
                    end

                    if (line_counter >= FB_HEIGHT) begin
                        activity_o <= 1'b0;
                        state <= HOLD;
                    end else begin
                        vram_sel_o      <= 1'b1;
                        vram_wr_o       <= 1'b1;
                        vram_addr_o     <= addr;
                        vram_data_out_o <= color;
                        state <= FILL1;
                        activity_o <= 1'b1;
                    end
                end
                
                FILL1: begin
                    if (vram_ack_i) begin
                        vram_sel_o <= 1'b0;
                        vram_wr_o  <= 1'b0;
                        addr       <= addr + 32'd1;
                        state      <= FILL2;
                        counter <= 16'h00FF;
                    end
                end

                FILL2: begin
                    counter <= counter - 1;
                    if (counter == 0)
                        state <= FILL0;
                end

                HOLD: begin
                    addr            <= 24'd0;
                    col_counter     <= 12'd0;
                    line_counter    <= 12'd0;
                    bg_color        <= bg_color + 12'h010;
                    state           <= FILL0;
                end
            endcase
        end
    end

endmodule
