import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(private http: HttpClient) {}
  login(data: any) {
    return this.http.post('http://127.0.0.1:8000/accounts/login/', data);
  }

  signup(data: any) {
    return this.http.post('http://127.0.0.1:8000/accounts/register/', data);
  }
}
