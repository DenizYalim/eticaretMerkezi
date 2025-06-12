import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Comment } from '../model/comment.type';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  http = inject (HttpClient);

  //comments : Array<Comment> = [{user: 'test', comment: 'testComment', platform: 'n11', rating:5}]

  constructor() {}

  getCommentsfromApi() {
    const url = 'http://127.0.0.1:5000/api/comments/3'
    return this.http.get<Array<Comment>>(url)
  }
}
