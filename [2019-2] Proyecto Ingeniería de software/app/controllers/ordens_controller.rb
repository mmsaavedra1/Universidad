class OrdensController < ApplicationController
  before_action :find_plato, only: [:new]

  def new
    @orden = @plato.ordens.build
  end

  def create
    @plato = Plato.find(params[:orden][:plato_id])
    @restaurante = Restaurante.find(params[:orden][:restaurante_id])

    @orden = @plato.ordens.build(orden_params)
    @orden.plato_id = @plato.id
    @orden.user_id = current_user.id
    @orden.restaurante_id = @restaurante.id
    @orden.precio = @plato.precio
    @orden.hora_llegada = Time.now + 60*rand(30..60)
    @orden.estado = "En proceso"

    if params[:orden][:notas] == nil
      @orden.nota = "-"
    end

    if @orden.save
      redirect_to restaurantes_path(@restaurante)
    else
      render 'new'
    end
  end

  def index
    @ordenes = Orden.all

    # Se actualizan los pedidos que fueron entregados
    @ordenes.each do |orden|
      if orden.estado == "En proceso" && orden.hora_llegada <= Time.now
        orden.estado = "Entregado"
        orden.save
      end
    end

  end

  def show
    @orden = Orden.find(params[:id])
    @orden.estado = "Cancelado"
    @orden.save

    redirect_to ordens_path
  end


  def destroy
  end

  private
  def orden_params
    params.require(:orden).permit(:direccion_de_envio, :notas)
  end

  def find_plato
    @plato = Plato.find(params[:plato_id])
  end

  def find_restaurante
    @restaurante = Restaurante.find(params[:orden][:restaurante_id])
  end
end
