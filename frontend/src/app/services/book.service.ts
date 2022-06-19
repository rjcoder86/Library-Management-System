import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class BookService {
  constructor(private http: HttpClient) {}

  getBooks() {
    return this.http.get('http://127.0.0.1:8000/api/allbooks/');
  }
  addBook(data: any) {
    return this.http.post('http://127.0.0.1:8000/api/addbook/', data);
  }
  deleteBook(id: number) {
    return this.http.get(`http://127.0.0.1:8000/api/deletebook/${id}`);
  }
}
