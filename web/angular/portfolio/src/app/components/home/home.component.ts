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

  ngOnInit(): void {
    window.addEventListener("scroll", () => {
      this.animateBoxes();
    })
  }
  ngAfterViewInit() {
    this.cargaCamaleon();
    this.cargarBolas();
  }

  cargarBolas() {
    let banner = document.querySelector(".banner-animated") as HTMLElement;
    let nBolas = 10;

    for (let n = 0; n < nBolas; n++) {
      let bola = document.createElement("div") as HTMLDivElement;
      bola.style.width = "50px";
      bola.style.height = "50px";
      bola.style.background = "rgba(17, 72, 223, 0.7)";
      bola.style.zIndex = "2";
      bola.style.opacity = ".5";
      bola.style.borderRadius = "50%";
      let positionY = Math.floor(Math.random() * (30 - 1 + 1)) + 1;
      let positionX = Math.floor(Math.random() * (30 - 1 + 1)) + 1;
      bola.style.gridColumnStart = positionX.toString();
      bola.style.gridRowStart = positionY.toString();
      bola.className = "bola";

      bola.onmouseover = () => {
        bola.style.transform = "scale(1.7)";
        bola.style.transition = "transform 0.3s ease-in-out";
        const color = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
        bola.style.background = color;
      };

      bola.onmouseout = () => {
        bola.style.transform = "scale(1)";
        bola.style.transition = "transform 3s ease-in-out, background 3s ease-in-out";
        const color = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
        bola.style.background = "rgba(17, 72, 223, 0.7)";
      };
      banner.appendChild(bola);

      let directionX = 1;
      let directionY = 1;
      let currentX = parseInt(bola.style.gridColumnStart) || 1;
      let currentY = parseInt(bola.style.gridRowStart) || 1;

      setInterval(() => {
        if (currentX + directionX > 30 || currentX + directionX < 1) {
          directionX *= -1;
        }
        if (currentY + directionY > 30 || currentY + directionY < 1) {
          directionY *= -1;
        }

        currentX += directionX;
        currentY += directionY;

        bola.style.gridColumnStart = currentX.toString();
        // bola.style.gridRowStart = currentY.toString();
      }, 50);
    }
  }



  animateBoxes(){
    const currentScroll = window.scrollY;
    const windowHeight = document.documentElement.scrollHeight;
    let animateBoxes = document.querySelectorAll(".info-boxes .content-boxes > *");
    console.log("SCROLL: " + currentScroll);
    console.log("Altura de pantalla: ", windowHeight);
    animateBoxes.forEach((box, index) => {
      const boxElement = box as HTMLDivElement;
      const boxTop = boxElement.getBoundingClientRect().top + window.scrollY;
      if (currentScroll + window.innerHeight > boxTop + 100) {
      boxElement.style.right = "0";
      boxElement.style.transition = `right 0.15s ease-in-out ${index * 0.2}s`;
      }
    });
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
