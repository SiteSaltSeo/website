import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { DinosaurComponent } from './components/dinosaur/dinosaur.component'

@NgModule({
  imports:      [ 
      BrowserModule,
      FormsModule,
      HttpModule
   
   ],
  declarations: [ 
    AppComponent,
    DinosaurComponent
     ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
