import { Component } from '@angular/core';
import {Header} from './components/header/header';
import {ListComponent} from './components/list/list';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [Header, ListComponent],
  template: '<app-header /> <app-list />',
  styleUrl: './app.css'
})
export class App {
  protected title = 'angular-project';
}
