import { ModuleWithProviders } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SimulacionComponent } from './components/simulacion/simulacion.component';
import { ErrorComponent } from './components/error/error.component';

const appRoutes: Routes = [
	{path: 'simulacion', component: SimulacionComponent},
	{path: '**', component: ErrorComponent}
];

export const appRoutingProviders: any[] = [];
export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);