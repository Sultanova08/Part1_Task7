def biggest_guy(a, b, c):
    list1 = ["a", "b" "c"]
    return max(list1)


def test_biggest_guy():
    try:
        assert biggest_guy(1, 3, 2) == 3
        assert biggest_guy(30, 10, 20) == 30
        assert biggest_guy(20, 10, 30) == 30
        assert biggest_guy(2, 1, 9) == 9
        assert biggest_guy("a", "a", "b") == "b"  # 'b' is greater than 'a'
    except (AssertionError) as e:
        print(e)
        print("Wrong!!")

    print("Correct buddy!!!")


test_biggest_guy()

