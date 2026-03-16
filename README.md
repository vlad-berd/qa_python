# Приложение BooksCollector.
### Позволяет установить жанр книг и добавить их в избранное.

#### :white_check_mark: Полностью (100%) покрыт класс юнит-тестами **BooksCollector** на Python 3 с использованием библиотеки pytest.

Тестовые методы class TestBooksCollector:
1. test_add_new_book_add_two_books
2. test_add_new_book_duplicate_name_book_not_added
3. test_add_new_book_negative_name_length_book_not_added
4. test_set_book_genre_book_and_genre_exists_genre_set
5. test_get_book_genre_exists_book_genre_received
6. test_get_books_with_specific_genre_exists_genre_books_list_received
7. test_get_books_with_specific_genre_no_exists_genre_books_list_no_received
8. test_get_books_genre_exist_books_returns_non_empty_dict
9. test_get_books_for_children_child_books_received
10. test_add_book_in_favorite_exists_book_book_added_to_favorites
11. test_add_book_in_favorites_duplicate_name_book_no_added_to_favorites
12. test_delete_book_from_favorites_exists_book_book_removed_from_favorites
13. test_get_list_of_favorites_books_success
14. test_get_list_of_favorites_books_exists_book_list_of_favorites_books_received

## Запустить тесты из терминала:

```sh
pytest -v tests.py
```
