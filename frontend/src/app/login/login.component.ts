import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  constructor(private userService: UserService, private router: Router) {}

  ngOnInit(): void {}
  onSubmit(form: NgForm) {
    const data = {
      email: form.value.email,
      password: form.value.password,
    };
    localStorage.setItem('email', form.value.email);
    localStorage.setItem('password', form.value.password);
    this.userService.login(data).subscribe(
      (response: any) => {
        console.log(response.is_admin);
        if (response.is_admin === true) {
          this.router.navigateByUrl('admin');
        } else {
          this.router.navigateByUrl('student');
        }
      },
      (errorMessage) => {
        console.log(errorMessage);
      }
    );
  }
}
