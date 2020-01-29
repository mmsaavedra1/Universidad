class SearchesController < ApplicationController
  def new
    @search = Search.new
  end

  def create
    @search = Search.create!(search_params)
    redirect_to search_path(@search, :opcion => params[:search][:opcion])
  end

  def show
    @search = Search.find(params[:id])
  end

  private
    def search_params
      params.require(:search).permit(:keyword, :ubicacion, :min_rating, :max_rating, :opcion)
    end
end
