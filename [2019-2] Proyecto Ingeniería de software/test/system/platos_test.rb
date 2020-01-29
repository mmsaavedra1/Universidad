require "application_system_test_case"

class PlatosTest < ApplicationSystemTestCase
  setup do
    @plato = platos(:one)
  end

  test "visiting the index" do
    visit platos_url
    assert_selector "h1", text: "Platos"
  end

  test "creating a Plato" do
    visit platos_url
    click_on "New Plato"

    fill_in "Cantidad personas sugeridas", with: @plato.cantidad_personas_sugeridas
    fill_in "Descripcion", with: @plato.descripcion
    fill_in "Nombre", with: @plato.nombre
    fill_in "Valoracion", with: @plato.valoracion
    click_on "Create Plato"

    assert_text "Plato was successfully created"
    click_on "Back"
  end

  test "updating a Plato" do
    visit platos_url
    click_on "Edit", match: :first

    fill_in "Cantidad personas sugeridas", with: @plato.cantidad_personas_sugeridas
    fill_in "Descripcion", with: @plato.descripcion
    fill_in "Nombre", with: @plato.nombre
    fill_in "Valoracion", with: @plato.valoracion
    click_on "Update Plato"

    assert_text "Plato was successfully updated"
    click_on "Back"
  end

  test "destroying a Plato" do
    visit platos_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Plato was successfully destroyed"
  end
end
