class PlatoReviewsController < ApplicationController
  before_action :find_plato
  before_action :find_plato_review, only: [:edit, :update, :destroy]
  before_action :authenticate_user!, only: [:new, :edit]

  def new
    @plato_review = PlatoReview.new
  end

  def create
    @plato_review = PlatoReview.new(plato_review_params)
    @plato_review.plato_id = @plato.id
    @plato_review.user_id = current_user.id

    if @plato_review.save
      redirect_to plato_path(@plato, :id_restaurante => params[:plato_review][:id_restaurante])
    else
      render 'new'
    end
  end

  def edit
    unless user_signed_in?
      redirect_to plato_path(@plato, :id_restaurante => restaurante)
    end

    unless  current_user.id == @plato_review.user_id
      redirect_to plato_path(@plato, :id_restaurante => restaurante)
    end
  end

  def update
    if @plato_review.update(plato_review_params)
      redirect_to plato_path(@plato, :id_restaurante => params[:plato_review][:id_restaurante])
    else
      render 'edit'
    end
  end

  def destroy
    @plato_review.destroy
    redirect_to plato_path(@plato, :id_restaurante => params[:id_restaurante])
  end

  private
    def plato_review_params
      params.require(:plato_review).permit(:rating, :comentario)
    end

    def find_plato
      @plato = Plato.find(params[:plato_id])
    end

    def find_plato_review
      @plato_review = PlatoReview.find(params[:id])
    end

  def find_restaurante
    restaurante = params[:id_restaurante]
  end

end
