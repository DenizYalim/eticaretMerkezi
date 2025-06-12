import { TestBed } from '@angular/core/testing';

import { CommentApiCall } from './comment-api-call';

describe('CommentApiCall', () => {
  let service: CommentApiCall;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CommentApiCall);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
