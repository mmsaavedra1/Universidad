class PlatosController < ApplicationController
  before_action :set_plato, only: [:show, :edit, :update, :destroy]
  before_action :actualizar_valoracion, only: [:index, :show]

  # GET /platos
  # GET /platos.json
  def index
    @platos = Plato.all
  end

  # GET /platos/1
  # GET /platos/1.json
  def show
    if @plato.plato_reviews.blank?
      @average_review = 0
    else
      @average_review = @plato.plato_reviews.average(:rating).round(2)
    end
  end

  # GET /platos/new
  def new
    @id_restaurante = params[:id_restaurante]
    @restaurante = Restaurante.find(@id_restaurante)
    @plato = @restaurante.platos.build
  end

  # GET /platos/1/edit
  def edit
  end

  # POST /platos
  # POST /platos.json
  def create
    @id_restaurante = params[:id_restaurante]
    @restaurante = Restaurante.find(@id_restaurante)
    @plato = @restaurante.platos.build(plato_params)

    if @plato.save
      redirect_to restaurante_path(@id_restaurante)
    else
      render :new
    end
  end

  # PATCH/PUT /platos/1
  # PATCH/PUT /platos/1.json
  def update
    @id_restaurante = params[:id_restaurante]

    if @plato.update(plato_params)
      redirect_to restaurante_path(@id_restaurante)
    else
      render :edit
    end
  end

  # DELETE /platos/1
  # DELETE /platos/1.json
  def destroy
    @id_restaurante = params[:id_restaurante]
    @plato.destroy

    redirect_to restaurante_path(@id_restaurante)
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_plato
      @plato = Plato.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def plato_params
      params.require(:plato).permit(:nombre, :descripcion, :cantidad_personas_sugeridas, :valoracion, :plato_img)
    end

  def actualizar_valoracion
    Plato.all.each do |plato|
      if plato.plato_reviews.blank?
        @average_review = 0
        plato.valoracion = 0
      else
        @average_review = plato.plato_reviews.average(:rating).round(2)
        plato.valoracion = @average_review
      end
      plato.save
    end
  end
end
