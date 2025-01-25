import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/auth';
import { Router } from '@angular/router';
import firebase from 'firebase';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private _currentUser: firebase.User;

  get currentUser(): firebase.User{
    return this._currentUser;
  }
  set currentUser(val: firebase.User) {
    this._currentUser = val;
  }

  constructor(private afAuth: AngularFireAuth, private router: Router, private httpClient: HttpClient) { }
  get isAuthenticated(): boolean {
    return this.afAuth.currentUser !== null;
  }

  signUp(email: string, password: string) {
    console.log('LOOK ', email)
    this.afAuth.createUserWithEmailAndPassword(email, password)
      .then(() => {
        // Sign up successful
        console.log('Success ', email)
        this.router.navigate(['/login']);

      })
      .catch((error) => {
        console.log('error ', error)
      });
  }

  login(email: string, password: string) {
    let self = this;
    this.afAuth.signInWithEmailAndPassword(email, password)
      .then(() => {
        self.currentUser = firebase.auth().currentUser
        if (self.currentUser) {
          let refreshToken = self.currentUser.refreshToken
          self.currentUser.getIdToken(/* forceRefresh */ true).then((idToken) => {
            // Send token to your backend via HTTPS
            console.log('idtoken')
            console.log(idToken)
            const headers = new HttpHeaders({
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${idToken}`
            });
            // Adjust the URL to your backend endpoint
            const backendUrl = '/api/voice/context';
            // Make an HTTP POST request to your backend with the ID token in the Authorization header
            let params = { 'role': 'system', 'action': 'replace', 'input_text': '' }
            //console.log(this.httpClient)
            // ...
          }).catch(function (error) {
            // Handle error
          });
          this.router.navigate(['/home']);
        }


      })
      .catch((error) => {
        // An error occurred
      });
  }

  logout() {
    this.afAuth.signOut()
      .then(() => {
        console.log('look at me ')
        this.router.navigate(['/login']);

      })
      .catch((error) => {
        // An error occurred
      });
  }
}