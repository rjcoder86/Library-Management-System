import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { BookService } from '../services/book.service';

@Component({
  selector: 'app-admin-page',
  templateUrl: './admin-page.component.html',
  styleUrls: ['./admin-page.component.css'],
})
export class AdminPageComponent implements OnInit {
  default = 'false';
  books: any;
  constructor(private bookService: BookService) {}

  ngOnInit(): void {
    this.bookService.getBooks().subscribe((res: any) => {
      console.log(res);
      this.books = res;
    });
  }
  onSubmit(form: NgForm) {
    const data = {
      book: form.value.book,
      author: form.value.author,
      book_type: form.value.book_type,
      is_issued: form.value.is_issued,
    };

    this.bookService.addBook(data).subscribe((response: any) => {
      form.reset();
      this.ngOnInit();
    });
  }
  deleteBook(id: number) {
    this.bookService.deleteBook(id).subscribe(() => {
      this.ngOnInit();
    });
  }
  // editBook(book: any) {
  //   const data = {
  //     id: book.id,
  //     book: book.book,
  //     author: book.author,
  //     book_type: book.book_type,
  //     is_issues: book.is_issued,
  //   };

  //   this.bookService.editBook(data).subscribe((response: any) => {
  //     console.log(response);
  //     this.ngOnInit();
  //   });
  // }
}
