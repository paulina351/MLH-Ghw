const pokedexInitButton = document.getElementById("pokedex-header-button");
const pokedexDoor = document.getElementById("pokedex-door");
const pokedexContent = document.getElementById("pokedex-content");
const pokedexImageContainer = document.getElementById("pokedex-image");
const prevButton = document.getElementById("prev-button");
const nextButton = document.getElementById("next-button");
const pageNumber = document.getElementById("page-number");

let currentPokemonId = 1;

pokedexInitButton.addEventListener("click", () => {
    if (pokedexDoor.classList.contains("close")) {
        pokedexDoor.classList.remove("close");
        pokedexDoor.classList.add("open");
    } else {
        pokedexDoor.classList.remove("open");
        pokedexDoor.classList.add("close");
    }
    //pokedexDoor.classList.toggle("open");
})

// Display position in pokedex
async function fetchPokemonById(pokemonId) {
    try {
        const response = await fetch('https://pokeapi.co/api/v2/pokemon/${pokemonId}');
        const pokemon = await response.json();
        displayPokemon(pokemon);
    } catch (error) {
        console.error("Error fetching Pokemon data:", error);
    }
}