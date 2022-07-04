import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class BookService {
  username = localStorage.getItem('email');
  password = localStorage.getItem('password');
  authorizationData = 'Basic ' + btoa(this.username + ':' + this.password);
  constructor(private http: HttpClient) {}

  getBooks() {
    let options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        Authorization: this.authorizationData,
      }),
    };
    return this.http.get('http://127.0.0.1:8000/api/allbooks/', options);
  }
  addBook(data: any) {
    let options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        Authorization: this.authorizationData,
      }),
    };
    return this.http.post('http://127.0.0.1:8000/api/addbook/', data, options);
  }
  deleteBook(id: number) {
    let options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        Authorization: this.authorizationData,
      }),
    };
    return this.http.get(`http://127.0.0.1:8000/api/deletebook/${id}`, options);
  }
  editBook(data: any) {
    let options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        Authorization: this.authorizationData,
      }),
    };
    return this.http.post(
      `http://127.0.0.1:8000/api/updatebook/${data.id}/`,
      options
    );
  }
}
