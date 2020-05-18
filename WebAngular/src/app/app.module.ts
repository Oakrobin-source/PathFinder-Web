import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
//import { HttpClientModule } from '@angular/common/http';
//import { FormsModule } from '@angular/forms';
//import { routing, appRoutingProviders } from './app.routing';

import { routing, appRoutingProviders } from './app.routing';
//import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SimulacionComponent } from './components/simulacion/simulacion.component';
import { ErrorComponent } from './components/error/error.component';
import { StoreModule } from '@ngrx/store';
import { reducers, metaReducers } from './reducers';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { environment } from '../environments/environment';

@NgModule({
  declarations: [
    AppComponent,
    SimulacionComponent,
    ErrorComponent
  ],
  imports: [
    BrowserModule,
    routing,
    StoreModule.forRoot(reducers, {
      metaReducers, 
      runtimeChecks: {
        strictStateImmutability: true,
        strictActionImmutability: true,
      }
    }),
    !environment.production ? StoreDevtoolsModule.instrument() : []
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
