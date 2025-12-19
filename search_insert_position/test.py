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
