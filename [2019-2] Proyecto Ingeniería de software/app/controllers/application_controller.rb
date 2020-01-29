class ApplicationController < ActionController::Base
  before_action :configure_permitted_parameters, if: :devise_controller?

  protected
  def configure_permitted_parameters
    devise_parameter_sanitizer.permit(:sign_in, keys:[:nombre, :direccion])
    devise_parameter_sanitizer.permit(:sign_up, keys: [:nombre, :direccion,  :email, :password, :password_confirmation])
    devise_parameter_sanitizer.permit(:account_update, keys: actualizar_datos)
  end

  private
  def actualizar_datos
    return [:nombre, :direccion, :email, :password, :current_password, :password_confirmation, :user_img]
  end

end