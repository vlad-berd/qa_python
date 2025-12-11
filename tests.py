import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2
    
    def test_add_new_book_duplicate_name_book_not_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['', 'ы' * 41, 'ы' * 45])
    def test_add_new_book_negative_name_length_book_not_added(self, collector, name):
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_book_and_genre_exists_genre_set(self, collector):
        collector.add_new_book('Девушка с татуировкой дракона')

        collector.set_book_genre('Девушка с татуировкой дракона', 'Детективы')

        assert collector.get_book_genre('Девушка с татуировкой дракона') == 'Детективы'
    
    def test_get_book_genre_exists_book_genre_received(self, collector):
        collector.add_new_book('Девушка с татуировкой дракона')
        collector.set_book_genre('Девушка с татуировкой дракона', 'Детективы')

        result = collector.get_book_genre('Девушка с татуировкой дракона')
        
        assert result == 'Детективы'
    
    def test_get_books_with_specific_genre_exists_genre_books_list_received(self, collector):
        collector.add_new_book('Тестовая книга 1')
        collector.add_new_book('Тестовая книга 2')
        collector.add_new_book('Тестовая книга 3')
        collector.set_book_genre('Тестовая книга 1', 'Детективы')
        collector.set_book_genre('Тестовая книга 2', 'Фантастика')
        collector.set_book_genre('Тестовая книга 3', 'Детективы')

        result = collector.get_books_with_specific_genre('Детективы')

        assert result == ['Тестовая книга 1', 'Тестовая книга 3']

    def test_get_books_with_specific_genre_no_exists_genre_books_list_no_received(self, collector):

        assert collector.get_books_with_specific_genre('Романы') == []
    
    def test_get_books_genre_success(self, collector):

        assert collector.get_books_genre() == {}
    
    def test_get_books_for_children_child_books_received(self, collector):
        collector.add_new_book('Взрослая книга')
        collector.add_new_book('Детская книга 1')
        collector.add_new_book('Детская книга 2')
        collector.set_book_genre('Взрослая книга', 'Ужасы')
        collector.set_book_genre('Детская книга 1', 'Мультфильмы')
        collector.set_book_genre('Детская книга 2', 'Фантастика')
        

        result = collector.get_books_for_children()
        
        assert result == ['Детская книга 1', 'Детская книга 2']
    
    def test_add_book_in_favorite_exists_book_book_added_to_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
    
    def test_add_book_in_favorites_duplicate_name_book_no_added_to_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1
    
    def test_delete_book_from_favorites_exists_book_book_removed_from_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_success(self, collector):

        assert collector.get_list_of_favorites_books() == []
