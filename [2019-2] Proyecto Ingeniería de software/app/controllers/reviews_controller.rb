class ReviewsController < ApplicationController
  before_action :find_restaurante
  before_action :find_review, only: [:edit, :update, :destroy]
  before_action :authenticate_user!, only: [:new, :edit]

  def new
    @review = Review.new
  end

  def create
    @review = Review.new(review_params)
    @review.restaurante_id = @restaurante.id
    @review.user_id = current_user.id

    if @review.save
      redirect_to restaurante_path(@restaurante)
    else
      render 'new'
    end
  end

  def edit
    unless user_signed_in?
      redirect_to restaurantes_url
    end

    unless current_user.id == @review.user_id
      redirect_to restaurantes_url
    end
  end

  def update
    if @review.update(review_params)
      redirect_to restaurante_path(@restaurante)
    else
      render 'edit'
    end
  end

  def destroy
    @review.destroy
    redirect_to restaurante_path(@restaurante)
  end

  private
    def review_params
      params.require(:review).permit(:rating, :comentario)
    end

    def find_restaurante
      @restaurante = Restaurante.find(params[:restaurante_id])
    end

  def find_review
    @review = Review.find(params[:id])
  end

end
