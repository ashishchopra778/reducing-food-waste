import React from 'react';

function Header() {
  return (
    <div>
      <nav class="navbar navbar-expand-lg fixed-top">
        <a class="navbar-brand" href="#">Cirrus Transit</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item m-1">
              <button class="bg-transparent btn btn-outline-light btn-block border-white rounded-pill">About</button>
            </li>
            <li class="nav-item m-1">
              <button class="bg-transparent btn btn-outline-light btn-block border-white rounded-pill">Sign up</button>
            </li>
          </ul> 
        </div>
      </nav>
    </div>
  )
}

export default Header;