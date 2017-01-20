import { Component, OnInit } from '@angular/core';
import { DinosaurService } from '../../services/dinosaur.service'

@Component({
  selector: 'dinosaurs',
  template: `<ul><li *ngFor="let dino of dinos"><a href="{{dino.url}}">{{dino.species}}</a></li></ul>`
})
export class DinosaurComponent implements OnInit {
  dinos: any[];
  error: any;

  constructor(private dinosaurService: DinosaurService) { }

  getDinos() {
    this.dinosaurService
        .getDinos()
        .then(dinos => this.dinos = dinos)
        .catch(error => this.error = error);
  }

  ngOnInit() {
    this.getDinos();
  }
}
