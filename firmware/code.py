import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType

kb = KMKKeyboard()

cols = (board.P0_02, board.P0_03, board.P0_28, board.P0_29, board.P0_04, board.P0_05)
rows = (board.P0_06, board.P0_08, board.P0_17, board.P0_20, board.P0_22, board.P0_24)

kb.col_pins = cols
kb.row_pins = rows
kb.diode_orientation = DiodeOrientation.COL2ROW

s = Split(split_type=SplitType.BLE, is_target_left=True)
kb.modules.append(s)

l0 = [
    KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,   KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T,        KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSLS,
    KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G,       KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B,       KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.ENT,
    KC.LCTL, KC.LALT, KC.LGUI, KC.MO(1), KC.SPC, KC.NO,  KC.NO, KC.SPC, KC.MO(1), KC.RGUI, KC.RALT, KC.RCTL,
                         KC.LEFT, KC.DOWN, KC.UP,  KC.DOWN, KC.UP, KC.RIGHT
]

l1 = [
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.DEL,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
                               KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS
]

kb.keymap = [l0, l1]

if __name__ == '__main__':
    kb.go()