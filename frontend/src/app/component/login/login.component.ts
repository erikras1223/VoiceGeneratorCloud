import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/service/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public username: string = "";
  public password: string = "";
  

  constructor(private afAuth: AuthService) { }

  ngOnInit(): void {
  }

  public login(event): void {
    this.afAuth.login(this.username, this.password)
    
  }

}
