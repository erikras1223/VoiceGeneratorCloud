import { Injectable } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/auth';
import { Router } from '@angular/router';
import firebase from 'firebase';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private afAuth: AngularFireAuth, private router:Router) { }
  get isAuthenticated(): boolean {
    return this.afAuth.currentUser !== null;
  }

  signUp(email: string, password: string) {
    console.log('LOOK ',email )
    this.afAuth.createUserWithEmailAndPassword(email, password)
      .then(() => {
        // Sign up successful
        console.log('Success ',email )
        this.router.navigate(['/login']);
        
      })
      .catch((error) => {
        console.log('error ',error )
      });
  }

  login(email: string, password: string) {
    this.afAuth.signInWithEmailAndPassword(email, password)
      .then(() => {
        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
          // Send token to your backend via HTTPS
          console.log('idtoken')
          console.log(idToken)
          // ...
        }).catch(function(error) {
          // Handle error
        });
        this.router.navigate(['/home']);
      })
      .catch((error) => {
        // An error occurred
      });
  }

  logout() {
    this.afAuth.signOut()
      .then(() => {
        // Logout successful

      })
      .catch((error) => {
        // An error occurred
      });
  }
}