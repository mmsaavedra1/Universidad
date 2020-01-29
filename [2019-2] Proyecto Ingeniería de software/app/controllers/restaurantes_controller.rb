class RestaurantesController < ApplicationController
  before_action :set_restaurante, only: [:show, :edit, :update, :destroy]
  before_action :authenticate_user!, only: [:new, :edit]
  before_action :actualizar_valoracion, only: [:index, :show]
  before_action :agregar_favorito, only: [:show]
  before_action :quitar_favorito, only: [:show]

  # GET /restaurantes
  # GET /restaurantes.json
  def index
    @restaurantes = Restaurante.search(params[:search])
  end

  # GET /restaurantes/1
  # GET /restaurantes/1.json
  def show
    if @restaurante.reviews.blank?
      @average_review = 0
    else
      @average_review = @restaurante.reviews.average(:rating).round(2)
    end
  end

  # GET /restaurantes/new
  def new
    if current_user.email == "admin@uc.cl"
      @restaurante = Restaurante.new
    else
      redirect_to restaurantes_url
    end
  end

  # GET /restaurantes/1/edit
  def edit
    unless user_signed_in?
      redirect_to restaurantes_url
    end

    unless current_user.email == @restaurante.correo
      redirect_to restaurantes_url
    end
  end

  # POST /restaurantes
  # POST /restaurantes.json
  def create
    @restaurante = Restaurante.new(restaurante_params)

    if @restaurante.save
      redirect_to @restaurante
    else
      render :new
    end
  end

  # PATCH/PUT /restaurantes/1
  # PATCH/PUT /restaurantes/1.json
  def update
      if @restaurante.update(restaurante_params)
        redirect_to @restaurante
      else
        render :edit
    end
  end

  # DELETE /restaurantes/1
  # DELETE /restaurantes/1.json
  def destroy
    @restaurante.destroy
    redirect_to restaurantes_url
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_restaurante
      @restaurante = Restaurante.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def restaurante_params
      params.require(:restaurante).permit(:nombre, :correo, :direccion, :valoracion, :numero_telefono, :restaurante_img)
    end

    def actualizar_valoracion
      Restaurante.all.each do |restaurante|
        if restaurante.reviews.blank?
          @average_review = 0
          restaurante.valoracion = 0
        else
          @average_review = restaurante.reviews.average(:rating).round(2)
          restaurante.valoracion = @average_review
        end
        restaurante.save
      end
    end

  # Crea restaurantes favoritos
  def agregar_favorito
    # Se crea el restaurante favorito si fue llamado el metodo
    if params[:nombre] == "agregar_favorito"
      if Favorito.where(:user_id => current_user.id, :restaurante_id => @restaurante.id).count == 0
        @favorito = Favorito.new(:user_id => current_user.id, :restaurante_id => @restaurante.id)
        @favorito.save
        redirect_to @restaurante
      end
    end
  end

  # Elimina restaurane favoritos
  def quitar_favorito
    if params[:nombre] == "quitar_favorito"
      @favorito = Favorito.where(:user_id => current_user.id, :restaurante_id => @restaurante.id)[0]
      @favorito.destroy
      redirect_to @restaurante
    end
  end
end
