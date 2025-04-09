import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ProjectsComponent } from './components/projects/projects.component';

export const routes: Routes = [
    {path:"",component:HomeComponent},
    {path:"proyectos",component:ProjectsComponent}
];
