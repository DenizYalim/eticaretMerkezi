import { Component, inject, OnInit, signal } from '@angular/core';
import { DataService } from '../../services/comment-api-call';
import { Comment } from '../../model/comment.type';


@Component({
  selector: 'app-list',
  templateUrl: `/list.html`
})
export class ListComponent implements OnInit {
  comment_api_cal_service = inject(DataService);
  comments = signal<Array<Comment>>([]);

  ngOnInit(): void {
    
    this.comment_api_cal_service
      .getCommentsfromApi()
      .subscribe((comments) => {
        this.comments.set(comments)
      })
  }
}
