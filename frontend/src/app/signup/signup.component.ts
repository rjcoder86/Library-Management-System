import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})

export class SignupComponent implements OnInit {
  isAdmin : boolean =false;
  constructor( private userService : UserService, private router : Router) { 

  }

  ngOnInit(): void {
  }
  onSubmit(form:NgForm){
    const data = {
      first_name: form.value.firstname,
      last_name: form.value.lastname,
      email: form.value.email,
      is_admin: form.value.isadmin,
      password: form.value.password,
    };


    this.userService.signup(data).subscribe(
      (response: any) => {
        console.log(response)
                 this.router.navigateByUrl('login');

      },
      (errorMessage) => {
       console.log(errorMessage)
      }
    );
  }

}
