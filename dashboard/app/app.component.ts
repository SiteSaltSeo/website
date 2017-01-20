import { Component } from '@angular/core';
import { DinosaurService } from './services/dinosaur.service'

@Component({
  selector: 'my-app',
  template: `<h1>Hello {{name}}<span *ngIf="itIsJuly">, DjangoCon</span>!</h1>
              <dinosaurs></dinosaurs>`,
  providers: [DinosaurService]
})

export class AppComponent {
  name:string = 'World'
  itIsJuly:boolean

  constructor() {
      var date = new Date()
      this.itIsJuly = (date.getMonth() == 12 && date.getFullYear() == 2016)
  }
}