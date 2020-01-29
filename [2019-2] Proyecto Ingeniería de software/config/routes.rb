Rails.application.routes.draw do
  resources :platos do
    resources :plato_reviews
  end
  resources :restaurantes do
    resources :reviews
  end
  devise_for :users
  resources :searches
  resources :ordens
  root 'restaurantes#index'
end
