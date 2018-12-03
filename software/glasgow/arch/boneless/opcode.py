OPCLASS_A      = 0b0000
OPCLASS_S      = 0b0001
OPCLASS_M      = 0b001
OPCLASS_I      = 0b01
OPCLASS_C      = 0b1

OPCODE_LOGIC   = 0b0000_0
OPTYPE_AND     = 0b00
OPTYPE_OR      = 0b01
OPTYPE_XOR     = 0b10

OPCODE_ARITH   = 0b0000_1
OPTYPE_ADD     = 0b00
OPTYPE_SUB     = 0b01
OPTYPE_CMP     = 0b10

OPCODE_SHIFT_L = 0b0001_0
OPTYPE_SLL     = 0b0
OPTYPE_ROT     = 0b1

OPCODE_SHIFT_R = 0b0001_1
OPTYPE_SRL     = 0b0
OPTYPE_SRA     = 0b1

OPCODE_LD      = 0b001_00
OPCODE_ST      = 0b001_01
OPCODE_LDX     = 0b001_10
OPCODE_STX     = 0b001_11

OPCODE_ADDI    = 0b01_000
OPCODE_MOVA    = 0b01_001
OPCODE_MOVL    = 0b01_010
OPCODE_MOVH    = 0b01_011
OPCODE_LDI     = 0b01_100
OPCODE_STI     = 0b01_101
OPCODE_JAL     = 0b01_110
OPCODE_JR      = 0b01_111

OPCODE_F_0     = 0b1_000
OPCODE_J       = (OPCODE_F_0<<1)|0

OPCODE_F_Z     = 0b1_001
OPCODE_JNZ     = (OPCODE_F_Z<<1)|0
OPCODE_JZ      = (OPCODE_F_Z<<1)|1
OPCODE_JNE     = OPCODE_JNZ
OPCODE_JE      = OPCODE_JZ

OPCODE_F_S     = 0b1_010
OPCODE_JNS     = (OPCODE_F_S<<1)|0
OPCODE_JS      = (OPCODE_F_S<<1)|1

OPCODE_F_O     = 0b1_011
OPCODE_JNO     = (OPCODE_F_O<<1)|0
OPCODE_JO      = (OPCODE_F_O<<1)|1

OPCODE_F_C     = 0b1_011
OPCODE_JNC     = (OPCODE_F_C<<1)|0
OPCODE_JC      = (OPCODE_F_C<<1)|1
OPCODE_JUGE    = OPCODE_JNC
OPCODE_JULT    = OPCODE_JC

OPCODE_F_CoZ   = 0b1_101
OPCODE_JUGT    = (OPCODE_F_CoZ<<1)|0
OPCODE_JULE    = (OPCODE_F_CoZ<<1)|1

OPCODE_F_SxO   = 0b1_110
OPCODE_JSGE    = (OPCODE_F_SxO<<1)|0
OPCODE_JSLT    = (OPCODE_F_SxO<<1)|1

OPCODE_F_SxOoZ = 0b1_111
OPCODE_JSGT    = (OPCODE_F_SxOoZ<<1)|0
OPCODE_JSLE    = (OPCODE_F_SxOoZ<<1)|1