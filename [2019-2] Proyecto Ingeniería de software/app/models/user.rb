class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  has_many :reviews
  has_many :plato_reviews
  has_many :ordens

  has_attached_file :user_img, {styles: { user_index: "200x200>", user_show: "200x200>" },
                                :url  => "/assets/images/user/:id/:style/:basename.:extension",
                                default_url: "usuario_sin_foto/missing.png"}
  validates_attachment_content_type :user_img, content_type: /\Aimage\/.*\z/
end
