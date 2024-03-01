import { AfterViewInit, ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { Queue } from '../util/queue';
import { trigger, state, style, animate, transition } from '@angular/animations';
import { AuthService } from '../service/auth.service';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent  {
  
  constructor(private authService: AuthService){
  }
  logout(event){
    this.authService.logout();
  }


}
