import { Component, ElementRef, ViewChild } from '@angular/core';
import { HeaderComponent } from '../header/header.component';
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  @ViewChild("camaleon") camaleon!: ElementRef;

  ngAfterViewInit() {
    this.cargaCamaleon();
  }

  cargaCamaleon() {
    let camaleon = this.camaleon.nativeElement as HTMLObjectElement;
    camaleon.addEventListener('load', () => {
      this.cambioColorRandom();
    });
  }

  cambioColorRandom() {
    setInterval(() => {
      const svgDoc = this.camaleon.nativeElement.contentDocument;
      const camaleon = svgDoc.querySelector('#camaleon') as SVGClipPathElement;
      const color = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
      camaleon.style.transition = 'fill 0.8s ease-in-out';
      camaleon.style.fill = color;
    },1000);
  }
}
