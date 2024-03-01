import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/service/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  public username: string
  public password: string;

  constructor(private authService:AuthService) { }

  ngOnInit(): void {
  }
  public signup(event){
    this.authService.signUp(this.username, this.password)
  }


}
