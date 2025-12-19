from search_insert_position.main import search

def test_should_return_0_if_list_is_empty():
    assert(search([], 4) == 0)

def test_should_return_index_if_target_was_found():
    assert(search([1], 1) == 0)

def test_should_found_target_at_left():
    assert(search([1, 2, 3, 4, 8, 9, 18, 100], 2) == 1)

def test_should_found_target_at_right():
    assert(search([1, 2, 3, 8, 9, 100, 150, 1000, 1100], 1000) == 7)

def test_should_found_target_going_left_and_right():
    assert(search([1, 2, 3, 6, 7, 8, 9], 5) == 3)

"""
    Target 5 
    nums = [1, 2, 3, 6, 7, 8, 9]

    middle = 0 + 6 = 6 / 2 = 3 
    nums[3] = 6

    5 = 6? no
    5 < 6? sí
    high = 3

    --
    middle = (0 + 3) / 2 = 1
    nums[1] = 2

    5 = 2? no
    5 < 2? no
    low = 1
    
    middle = math.floor((1+3) / 2) = 2
    5 = 3? No.
    5 < 3? No.
    low = 2

    --
    middle = math.floor((2+3) / 2) = 2
    ¡Acá se me rompió mi código! 
    El problema es que caigo en 2 siempre. Entonces, a middle siempre le tengo que agregar una unidad porque middle en la próxima ya no es candidato.
"""