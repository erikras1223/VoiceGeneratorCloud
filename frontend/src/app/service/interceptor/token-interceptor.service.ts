import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from "@angular/common/http";
import { Injectable } from "@angular/core";
import firebase from "firebase";
import { Observable, from } from "rxjs";
import { mergeMap } from 'rxjs/operators';

@Injectable({
    providedIn: 'root'
  })
  export class TokenInterceptor implements HttpInterceptor {
    constructor() {}
    /*
    * Every outgoing Http request will go through this Http interceptor and append
    * Authorization nav-header to it.
    */
    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>>  {
      /* Firebase will refresh token automatically if expired */
      return from(this.getCurrentIdToken()).pipe(
        mergeMap((token: string| null) => {
          console.log(token);
          req = req.clone({
            setHeaders: {
              Authorization: `Bearer ${token}`
            }
          });
          return next.handle(req);
        })
      )
    }
  
    getCurrentIdToken(): Promise<string | null> {
      return new Promise((resolve, reject) => {
        const auth = firebase.auth();
        const unsubscribe = auth.onIdTokenChanged(user => {
          unsubscribe();
          if (user) {
            user.getIdToken().then(token => {
              resolve(token);
            });
          } else {
            resolve(null);
          }
        }, reject);
      });
    }
  }

