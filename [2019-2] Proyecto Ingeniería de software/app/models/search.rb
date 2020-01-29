class Search < ApplicationRecord
  def restaurante
    @restaurante ||= find_restaurante
  end

  def plato
    @plato ||= find_plato
  end

  private
    def find_restaurante
      restaurantes = Restaurante.all.order(:nombre)
      restaurantes = restaurantes.where("nombre LIKE ?", "%#{keyword}%") if keyword.present?
      restaurantes = restaurantes.where("direccion LIKE ?", "%#{ubicacion}%") if ubicacion.present?
      restaurantes = restaurantes.where("valoracion >= ?", min_rating) if min_rating.present?
      restaurantes = restaurantes.where("valoracion <= ?", max_rating) if max_rating.present?
      restaurantes
    end

    def find_plato
      platos = Plato.all.order(:nombre)
      platos = platos.where("nombre LIKE ?", "%#{keyword}%") if keyword.present?
      platos = platos.where("descripcion LIKE ?", "%#{ubicacion}%") if ubicacion.present?
      platos = platos.where("valoracion >= ?", min_rating) if min_rating.present?
      platos = platos.where("valoracion <= ?", max_rating) if max_rating.present?
      platos
    end
end
