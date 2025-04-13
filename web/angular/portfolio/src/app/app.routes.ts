import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ProjectsComponent } from './components/projects/projects.component';
import { BlogComponent } from './components/blog/blog.component';
import { ContactoComponent } from './components/contacto/contacto.component';
import { NotfoundComponent } from './components/notfound/notfound.component';
export const routes: Routes = [
    {path:"",component:HomeComponent},
    {path:"proyectos",component:ProjectsComponent},
    {path:"blog",component:BlogComponent},
    {path:"contact",component:ContactoComponent},
    {path:"**",component:NotfoundComponent}
];
