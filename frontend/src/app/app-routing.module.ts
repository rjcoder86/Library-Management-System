import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { StudentPageComponent } from './student-page/student-page.component';

const routes: Routes = [
  {path : '' ,redirectTo:'login',pathMatch:'full'},
  { path : 'login',component:LoginComponent},
  { path : 'signup',component:SignupComponent},
  { path : 'admin',component:AdminPageComponent},
  { path : 'student',component:StudentPageComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
