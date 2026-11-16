# Dữ liệu dùng chung cho PDF (make.py) và web (web_build.py).
# Thêm màn mới: viết file nguồn manX.txt rồi thêm 1 mục vào ACTS bên dưới.
LUMINE = dict(name='Lumine', role='Nhân vật chính · Nhà Lữ Hành', img='lumine_icon.png',
  desc='Nhà Lữ Hành đến từ thế giới khác. Bị vị thần lạ mặt phong ấn và cướp mất người anh song sinh, cô bắt đầu hành trình đi tìm Bảy Vị Thần của Teyvat.')
PAIMON = dict(name='Paimon', role='Bạn đồng hành', img='paimon.png', desc='Được Lumine cứu khỏi chết đuối hai tháng trước, Paimon tự nhận làm người dẫn đường cho cô. Hay ăn, hay nói, và rất ghét bị gọi là “thực phẩm dự trữ”.')
AETHER = dict(name='Aether', role='Anh trai song sinh của Lumine', img='aether_icon.png', desc='Bị vị thần lạ mặt mang đi trong ngày hai anh em định rời khỏi thế giới này. Là người mà Lumine đang tìm kiếm.')
GOD = dict(name='Vị Thần Lạ Mặt', role='Bí ẩn', desc='Tự xưng là “người duy trì thiên lý”. Đã chặn đường cặp song sinh, phong ấn Lumine và đem Aether đi.')
AMBER = dict(name='Amber', role='Kỵ Sĩ Trinh Thám · Đội Kỵ Sĩ Tây Phong', img='amber_icon.png', desc='Cô gái nhiệt huyết, Kỵ Sĩ Trinh Thám cuối cùng của Đội Kỵ Sĩ. Gặp Lumine trên đường đến Mondstadt, đã hộ tống cô vào thành và tặng cô Phong Chi Dực.')
KAEYA = dict(name='Kaeya', role='Đội Trưởng Kỵ Binh · Đội Kỵ Sĩ Tây Phong', img='kaeya_icon.png', desc='Kiếm sĩ có vẻ ngoài ngoại quốc với miếng bịt mắt, lời nói luôn nửa đùa nửa thật. Đã chứng kiến Lumine đẩy lui Phong Ma Long.')
JEAN = dict(name='Jean', role='Đội Trưởng Đại Diện · Đội Kỵ Sĩ Tây Phong', img='jean_icon.png', desc='“Người Thủ Hộ Mondstadt”, đang gánh vác Đội Kỵ Sĩ khi đại đội trưởng đi xa. Người lên kế hoạch thanh lý ba ngôi đền Tứ Phong Thủ Hộ.')
LISA = dict(name='Lisa', role='Quản lý thư viện · Đội Kỵ Sĩ Tây Phong', img='lisa_icon.png', desc='Ma pháp sư thông thái nhưng có phần biếng nhác. Nhờ ma pháp của cô mà Đội Kỵ Sĩ tìm ra nguồn gốc cơn bão.')
DRAGON = dict(name='Phong Ma Long', role='Mối đe dọa của Mondstadt', img='dvalin_icon.png', desc='Con rồng khổng lồ màu xanh thường xuất hiện quanh Mondstadt, gây ra bão tố và tấn công thẳng vào thành.')
BOY = dict(name='Thiếu niên bí ẩn', role='Chưa rõ danh tính', desc='Người được Lumine và Paimon bắt gặp đang nói chuyện với con rồng trong rừng.')
VOICE = dict(name='Âm Thanh Thần Bí', role='Chưa rõ danh tính', desc='Giọng nói đã dùng “gió ngàn năm” nâng đỡ Lumine trong trận chiến với Phong Ma Long.')
REDHAIR = dict(name='Người đàn ông tóc đỏ', role='Chưa rõ danh tính', desc='Xuất hiện sau khi Lumine rời Đền Sói Bắc Phong, hạ gục Pháp Sư Vực Sâu trước mặt Kaeya.')
MAGE = dict(name='Pháp Sư Vực Sâu', role='Kẻ đứng sau', desc='Kẻ đã giật dây đám Hilichurl phục kích ở Đền Sói Bắc Phong.')
DVALIN = dict(name='Dvalin', role='Tên thật của Phong Ma Long', img='dvalin_icon.png', desc='Theo lời Lisa, Dvalin từng là Rồng Đông Phong trong Tứ Phong Thủ Hộ trước khi bị gọi là Ma Long.')

VENTI = dict(name='Venti', role='Nhà thơ lang thang', img='venti_icon.png', desc='Thiếu niên mặc đồ xanh từng nói chuyện với Dvalin trong rừng. Tự xưng là nhà thơ lang thang giỏi nhất thế gian, có mối liên hệ kỳ lạ với Nguyên Tố Phong, muốn dùng Đàn Thiên Không để cứu Dvalin.')
DILUC = dict(name='Diluc', role='Chủ Tửu Trang Dawn', img='diluc_icon.png', desc='Ông chủ lớn đứng sau quán rượu Quà Tặng Của Thiên Sứ, không ưa Đội Kỵ Sĩ nhưng ra tay che giấu và giúp nhóm Lumine lấy lại Đàn Thiên Không.')
ANASTASIA = dict(name='Anastasia', role='Quan ngoại giao Fatui', desc='Sứ giả Fatui của Snezhnaya, đòi Đội Kỵ Sĩ giao việc phòng thủ Mondstadt cho Fatui nếu không thể tiêu diệt Ma Long.')
GOTELINDE = dict(name='Gotelinde', role='Tu nữ Đại Giáo Đường', desc='Tu nữ từ chối cho Venti và Lumine mượn Đàn Thiên Không khi không có văn bản xác nhận.')
SIGNORA = dict(name='Signora', role='Quan Chấp Hành thứ 8 của Fatui', desc='Chỉ được nhắc đến qua lời đe dọa của thủ vệ Fatui và lời giải thích của Diluc. Chưa xuất hiện trực tiếp.')
MAGE2 = dict(name='Pháp Sư Vực Sâu', role='Giáo Đoàn Vực Sâu', desc='Kẻ dùng lời nguyền ăn mòn tâm trí Dvalin, phá hỏng cuộc gặp ở Vực Hái Sao và nhắc đến một kẻ mà hắn gọi là “Điện hạ”.')
DVALIN2 = dict(name='Dvalin', role='Phong Ma Long · Rồng Đông Phong', img='dvalin_icon.png', desc='Nước mắt của nó kết tinh thành những viên đá đỏ. Theo Venti, nó bị máu độc của ác long và lời nguyền Vực Sâu hành hạ, chứ không tự sinh ra thù hận.')

# --- Màn III ---
VENTI3 = dict(name='Venti', role='Nhà thơ lang thang · Phong Thần Barbatos', img='venti_icon.png', desc='Nhà thơ lang thang, cũng chính là Phong Thần Barbatos. Tự nhận mình là “người yếu nhất trong bảy vị thần”, dẫn sức mạnh Nguyên Tố Phong cho Lumine trong trận chiến cứu Dvalin.')
DILUC3 = dict(name='Diluc', role='Chủ Tửu Trang Dawn', img='diluc_icon.png', desc='Dùng mạng lưới tình báo tìm ra dấu vết Pháp Sư Vực Sâu gần Tửu Trang, rồi cùng nhóm Lumine tiến vào Phế Tích Phong Long.')
JEAN3 = dict(name='Jean', role='Đội Trưởng Đại Diện · Đội Kỵ Sĩ Tây Phong', img='jean_icon.png', desc='Sẵn sàng làm “kỵ sĩ xung phong lên trước”, cùng Lumine vào Phế Tích Phong Long và đứng ra giải thích hiểu lầm về Dvalin cho người dân.')
DVALIN3 = dict(name='Dvalin', role='Phong Ma Long · Rồng Đông Phong', img='dvalin_icon.png', desc='Bị lời nguyền Vực Sâu thao túng, rút về sào huyệt ở Phế Tích Phong Long. Được Lumine giải thoát và Venti chúc phúc để “bay tự do thêm nữa”.')
MAGE3 = dict(name='Pháp Sư Vực Sâu', role='Giáo Đoàn Vực Sâu', desc='Kẻ cản trở cuộc gặp ở Vực Hái Sao, bị nhóm Lumine săn lùng và hạ gục gần Tửu Trang.')
AMBER3 = dict(name='Amber', role='Kỵ Sĩ Trinh Thám · Đội Kỵ Sĩ Tây Phong', img='amber_icon.png', desc='Ở lại giữ Mondstadt trước cuộc tấn công bất thường của Hilichurl, rồi mời Lumine ăn Thịt Nướng Mật Ong mừng chiến thắng.')
KAEYA3 = dict(name='Kaeya', role='Đội Trưởng Kỵ Binh · Đội Kỵ Sĩ Tây Phong', img='kaeya_icon.png', desc='Âm thầm cố thủ trong thành, đánh kẻ xâm nhập của Giáo Đoàn Vực Sâu và biết được chúng có một kẻ chỉ đạo gọi là “Hoàng tử điện hạ”.')
BARBARA = dict(name='Barbara', role='Mục sư tế lễ · Giáo hội Tây Phong', img='barbara_icon.png', desc='Chuyên viên phụ trách thu hồi Đàn Thiên Không của giáo hội. Đã chữa trị cho Lumine và Venti khi hai người bất tỉnh bên ngoài Giáo Đường.')
SIGNORA3 = dict(name='Signora', role='Quan Chấp Hành thứ 8 của Fatui', img='signora_icon.png', desc='Phục kích Venti bên ngoài Đại Giáo Đường và cướp đi Gnosis của Phong Thần.')

# --- Chương I · Màn I (Liyue) ---
CHILDE = dict(name='Childe', role='Quan Chấp Hành Fatui', img='childe_icon.png', desc='Chàng trai trẻ đã kéo Lumine thoát khỏi vòng vây Thiên Nham Quân. Tự nhận là Quan Chấp Hành Fatui, đưa cho cô tín vật để đi tìm tiên nhân ở Tuyệt Vân Gián.')
NINGGUANG = dict(name='Ningguang', role='“Thiên Quyền” của Thất Tinh Liyue', img='ningguang_icon.png', desc='Người chủ trì Điển Lễ Thỉnh Tiên. Khi tiên thể của Đế Quân rơi xuống, cô ra lệnh bao vây toàn bộ Ngọc Kinh Đài.')
REX = dict(name='Nham Vương Đế Quân', role='Nham Thần Morax', desc='Vị thần lâu đời nhất trong bảy vị thần, thần của khế ước. Tiên thể của ngài rơi xuống đài tế giữa Điển Lễ Thỉnh Tiên, không còn hơi thở.')
MOONCARVER = dict(name='Tước Nguyệt Trúc Dương Chân Quân', role='Tiên nhân ở Tuyệt Vân Gián', img='mooncarver.png', desc='Tam Nhãn Ngũ Hiển Tiên Nhân đầu tiên Lumine gặp. Đẩy lui Thiên Nham Quân rồi nhờ cô đi báo tin cho các tiên nhân khác.')
XIAO = dict(name='Xiao', role='Hộ Pháp Dạ Xoa · Hàng Ma Đại Thánh', img='xiao_icon.png', desc='Tiên nhân xuất hiện ở Nhà Trọ Vọng Thư. Lạnh lùng xua người trần đi, nhưng thích món đậu hũ hạnh nhân.')
GOLDET = dict(name='Verr Goldet', role='Chủ Nhà Trọ Vọng Thư', desc='Người Mondstadt làm chủ nhà trọ. Chỉ cho Lumine cách “dỗ Xiao vui vẻ” và cách đối phó với hồn ma trong quán.')
YANXIAO = dict(name='Yanxiao', role='Đầu bếp Nhà Trọ Vọng Thư', desc='Đầu bếp trông dữ tợn nhưng sợ ma, chỉ chịu làm đậu hũ hạnh nhân sau khi hồn ma hứa không quậy nữa.')
MING = dict(name='Bé Ming', role='Hồn ma nhỏ ở nhà trọ', desc='Linh hồn cô bé hay hát, trêu chọc khách trọ cho đến khi bị Lumine bắt được.')
MOUNTAIN = dict(name='Lí Thủy Điệp Sơn Chân Quân', role='Tiên nhân ở Hổ Lao Sơn', img='mountainshaper.png', desc='Vị tiên nhân trồng hoa “Đạc Sơn Quy” sinh ra Hổ Phách để giữ sơn môn thanh tịnh.')
CLOUD = dict(name='Lưu Vân Tá Phong Chân Quân', role='Tiên nhân ở Âu Tàng Sơn', img='cloudretainer.png', desc='Vị tiên nhân giỏi “cơ quan thuật”, suýt đi “trấn áp” Cảng Liyue khi nghe tin Đế Quân bị ám sát.')
LIDING = dict(name='Li Ding và Li Dang', role='Hai anh em lên Hổ Lao Sơn', desc='Lên núi tìm bảo vật trong Hổ Phách, một người bị Hổ Phách nhốt lại và được Lumine cứu ra.')

# --- Chương I · Màn IV (Giới Thiệu + Màn IV) ---
KATHERYNE = dict(name='Katheryne', role='Hiệp Hội Nhà Mạo Hiểm Mondstadt', desc='Người tiếp tân của hiệp hội, kể cho Lumine về vị khách lạ mặt tóc vàng đeo bịt mắt vừa đến Mondstadt.')
DAIN_GT = dict(name='Dainsleif', role='Nhà mạo hiểm tự do', img='dainsleif_icon.png', desc='Người lạ mặt tóc vàng đeo bịt mắt. Nhận lời đồng hành với giá 500 Mora và ba câu hỏi, chỉ nhận ủy thác liên quan đến Giáo Đoàn Vực Sâu.')
CHARLES = dict(name='Charles', role='Người pha chế quán Quà Tặng Của Thiên Sứ', desc='Cho Lumine biết vị khách lạ “rất sành về rượu” và hẹn tối nay sẽ đến lấy rượu.')
LAWRENCE = dict(name='Lawrence và Wagner', role='Kỵ sĩ gác cổng · Thợ rèn', desc='Hai người dân Mondstadt chỉ đường cho Lumine lần theo dấu vết người lạ mặt.')
DAIN4 = dict(name='Dainsleif', img='dainsleif_icon.png', role='“Kiếm Sĩ Hoàng Hôn” của Khaenri\'ah', desc='Cùng Lumine truy tìm Sứ Đồ Vực Sâu và phá kế hoạch “lay chuyển thần tọa”. Theo lời Aether, anh là hộ vệ cung đình Khaenri\'ah đời cuối, mang lời nguyền bất tử.')
GANYU4 = dict(name='Ganyu', role='Thư ký của Thất Tinh Liyue', img='ganyu_icon.png', desc='Treo ủy thác ở hiệp hội vì lo lắng Đạo Bảo Đoàn động vào di tích của Giáo Đoàn Vực Sâu.')
LAN = dict(name='Lan', role='Hiệp Hội Nhà Mạo Hiểm Liyue', desc='Cùng Ganyu kể cho Lumine về “Nam Trưởng Tỷ”, “Bắc Quái Điểu” và “Trùm Đạo Bảo”.')
HERALD = dict(name='Sứ Đồ Vực Sâu', img='herald_icon.png', role='Giáo Đoàn Vực Sâu', desc='Thống lĩnh của Pháp Sư Vực Sâu, kẻ đứng sau kế hoạch “Máy dệt vận mệnh”. Gọi Aether là “Hoàng tử điện hạ”.')
ROSARIA = dict(name='Rosaria', role='Nữ tu Giáo Hội Tây Phong', img='rosaria_icon.png', desc='Báo tin Giáo Đoàn Vực Sâu tập họp ở Lang Lãnh.')
RAZOR = dict(name='Razor', role='Thiếu niên của bầy sói', img='razor_icon.png', desc='Bảo vệ linh hồn Vua Sói Bắc Phong trước nghi thức của Sứ Đồ Vực Sâu.')
BOREAS = dict(name='Vua Sói Bắc Phong', img='boreas_icon.png', role='Linh hồn Ma Thần Andrius · Boreas', desc='Chủ nhân Lang Lãnh. Kể về cỗ máy từng xông vào bãi tập luyện của mình — manh mối về “máy cày đầu tiên của thế giới”.')
AETHER4 = dict(name='Aether', role='Anh trai song sinh của Lumine · “Hoàng tử điện hạ”', img='aether_icon.png', desc='Xuất hiện bên cạnh Sứ Đồ Vực Sâu, gọi Dainsleif là kẻ thù và hẹn với Lumine: “Chúng ta ắt sẽ trùng phùng.”')
JEAN4 = dict(name='Jean', role='Đội Trưởng Đại Diện · Đội Kỵ Sĩ Tây Phong', img='jean_icon.png', desc='Dẫn quân đối phó Giáo Đoàn Vực Sâu ở Lang Lãnh, nhờ Lumine đi xem Vua Sói có gặp nguy hiểm không.')
BARBARA4 = dict(name='Barbara', role='Mục sư tế lễ · Giáo hội Tây Phong', img='barbara_icon.png', desc='Kể chuyện “Thất Thiên Thần Tượng mất tích” và “oán hận của bạo quân”.')


# --- Chương I · Màn II (Liyue) ---
ZHONGLI = dict(name='Zhongli', role='Khách của Vãng Sinh Đường', img='zhongli_icon.png', desc='Người “trong nghề” được Childe giới thiệu. Am hiểu mọi phong tục của Liyue nhưng luôn quên mang tiền, mời Lumine cùng chuẩn bị Điển Lễ Tiễn Tiên cho Nham Vương Đế Quân.')
CHILDE2 = dict(name='Childe', role='Quan Chấp Hành Fatui', img='childe_icon.png', desc='Giữ lời hứa tìm “người có thể phá vỡ cục diện”, chi tiền cho Điển Lễ Tiễn Tiên, nhưng âm thầm cho người nghe ngóng chuyện Hoàng Kim Ốc.')
EKATERINA = dict(name='Ekaterina', role='Nhân viên Ngân hàng Bắc Quốc', desc='Người của Fatui ở quầy Ngân hàng Bắc Quốc, chỉ đường cho Lumine đến Lưu Ly Đình và nghe lén giúp Childe.')
SHITOU = dict(name='Shitou', role='Chủ tiệm ngọc Giải Thúy Hàng', desc='Ông chủ tiệm ngọc keo kiệt, nhưng chỉ lấy nửa giá rương Dạ Phách Thạch khi biết nó dùng để tiễn Nham Vương Gia.')
YINGER = dict(name="Ying'er", role='Người làm Sáp Thơm ở Xuân Hương Diêu', desc='Cô gái hay trêu chọc, đã cùng Lumine nấu ba loại Sáp Thơm từ Hoa Nghê Thường ở bếp Vạn Dân Đường.')
PING = dict(name='Bình Lão Lão', role='Người giữ Chuông Tẩy Trần', img='ping_icon.png', desc='Bà lão sống trên Ngọc Kinh Đài, cất “tất cả tài sản” trong một chiếc ấm thần kỳ. Bạn cũ của Zhongli.')
QIQI = dict(name='Qiqi', role='Nhân viên Nhà Thuốc Bubu', img='qiqi_icon.png', desc='Cô bé cương thi chỉ hành động theo “mệnh lệnh” tự đặt cho mình, nhờ nhóm Lumine đi bắt “Dê Dừa” để đổi lấy Hương Bất Tử.')
BAIZHU = dict(name='Baizhu', role='Chủ Nhà Thuốc Bubu', img='baizhu_icon.png', desc='Ông chủ nhà thuốc cùng con rắn biết nói Changsheng. Bán Hương Bất Tử giá 299 vạn Mora sau khi bắt tay với Childe.')
GANYU = dict(name='Ganyu', role='Thư ký Nguyệt Hải Đình', img='ganyu_icon.png', desc='Thư ký của toàn thể Thất Tinh, sứ giả đặc biệt của Ningguang. Tìm đến quán Ba Cốc Say Mèm để trao thư mời Lumine đến Quần Ngọc Các.')
# --- Chương I · Màn III (Liyue) ---
KEQING_C3 = dict(name='Keqing', role='“Ngọc Hành Tinh” của Thất Tinh Liyue', img='keqing_icon.png', desc='Gặp Lumine bên máy Guizhong ở Thiên Hoành Sơn. Thẳng thắn, “bất kính với thần tiên”, tin rằng thời đại của tiên nhân đã qua.')
NINGGUANG_C3 = dict(name='Ningguang', role='“Thiên Quyền” của Thất Tinh Liyue', img='ningguang_icon.png', desc='Mời Lumine lên Quần Ngọc Các, chỉ cho cô dấu vết nghiên cứu Bách Vô Cấm Kỵ Lục của Fatui. Từ bỏ Quần Ngọc Các để trấn áp Ma Thần.')
GANYU_C3 = dict(name='Ganyu', role='Thư ký Nguyệt Hải Đình', img='ganyu_icon.png', desc='Sứ giả của Thiên Quyền Tinh, con lai giữa loài người và Kỳ Lân. Tặng Bách Hợp Lưu Ly cho Điển Lễ Tiễn Tiên.')
ZHONGLI_C3 = dict(name='Zhongli', role='Khách của Vãng Sinh Đường', img='zhongli_icon.png', desc='Cùng Lumine đi chặng cuối chuẩn bị Điển Lễ Tiễn Tiên, hiểu biết sâu rộng về lịch sử Liyue.')
CHILDE_C3 = dict(name='Childe', role='Quan Chấp Hành Fatui', img='childe_icon.png', desc='Tìm đến Hoàng Kim Ốc để đoạt Gnosis, giao chiến với Lumine, rồi dùng Bách Vô Cấm Kỵ Lục đánh thức Ma Thần Osial.')
SIGNORA_C3 = dict(name='Signora', role='Quan Chấp Hành thứ 8 của Fatui', img='signora_icon.png', desc='Kẻ từng cướp Gnosis của Phong Thần ở Mondstadt, xuất hiện trở lại ở Ngân Hàng Bắc Quốc tại Liyue.')
XIAO_C3 = dict(name='Xiao', role='Hộ Pháp Dạ Xoa · Hàng Ma Đại Thánh', img='xiao_icon.png', desc='Cùng các tiên nhân lên Quần Ngọc Các chống lại Ma Thần Lốc Xoáy.')
ADEPTI_C3 = dict(name='Ba vị Chân Quân', role='Tiên nhân Tuyệt Vân Gián', desc='Tước Nguyệt Trúc Dương, Lưu Vân Tá Phong và Lí Thủy Điệp Sơn Chân Quân đến Liyue hỏi tội Thất Tinh, rồi cùng Thất Tinh chống lại Ma Thần.')
PING_C3 = dict(name='Bình Lão Lão', role='Tiên nhân', desc='Lên tiếng bênh vực Ningguang và khuyên các tiên nhân hãy nhìn vào con người Liyue.')
OSIAL = dict(name='Osial', role='Ma Thần Lốc Xoáy', img='osial.png', desc='Ma Thần thất bại dưới tay Morax trong chiến tranh ma thần, bị trấn áp dưới Cô Vân Các, bị Childe đánh thức.')
MENGDAN = dict(name='Meng Dan', role='Người cung cấp hàng cho Minh Tinh Trai', desc='Bị Đạo Bảo Đoàn nhốt trong di tích, được Lumine cứu và tặng hộp đựng quà.')
# --- Màn III.1 (Razor) ---
RAZOR41 = dict(name='Razor', role='Thiếu niên được bầy sói nuôi lớn', img='razor_icon.png', desc='Sống cùng “Lupical” — bầy sói ở Lang Lãnh. Bị dân làng nghi là kẻ đứng sau vụ sói tập kích Thanh Tuyền Trấn.')
AMBER41 = dict(name='Amber', role='Kỵ Sĩ Trinh Thám · Đội Kỵ Sĩ Tây Phong', img='amber_icon.png', desc='Điều tra vụ đàn sói tập kích đội xe và Thanh Tuyền Trấn. Razor không nhớ tên cô, chỉ gọi là “cô gái màu đỏ”.')
BOREAS41 = dict(name='Vua Sói Bắc Phong', role='Lãnh chúa của Lang Lãnh · Boreas', img='boreas_icon.png', desc='“Ngài ấy” mà Razor nhắc đến. Người đặt ra cái tên “Lupical”.')
VILLAGERS41 = dict(name='Hopkins Thần Kỳ và Jotun', role='Dân Thanh Tuyền Trấn', desc='Muốn tự tay trả thù đàn sói sau vụ tập kích, gọi Razor là “người được sói nuôi lớn”.')
DRAFF = dict(name='Draff và Siegfria', role='Thợ săn ở Thanh Tuyền Trấn · Người đánh xe', desc='Draff lo cho những người trẻ dễ tức giận; Siegfria kể lại vụ đàn sói tập kích thị trấn.')

# --- Màn III.2 (Amber) ---
AMBER42 = dict(name='Amber', role='Kỵ Sĩ Trinh Thám · Quán Quân Bay Lượn', img='amber_icon.png', desc='Làm giám khảo kỳ thi bằng bay lượn của Lumine. Cầm nhầm quyển truyện ngụ ngôn về con chim nhỏ học bay thay cho sách hướng dẫn.')
OTTO = dict(name='Otto', role='Kỵ sĩ Đội Kỵ Sĩ Tây Phong', desc='Chặn Lumine lại để kiểm tra bằng bay lượn, kể về tên trộm “Quái Điểu” vừa đem văn vật của giáo đường trốn mất.')
RAPTOR = dict(name='Quái Điểu', role='Tội phạm của Thành Mondstadt', desc='Thường dùng Phong Chi Dực để gây án. Đội Kỵ Sĩ chưa đuổi kịp hắn lần nào.')
FARRAH = dict(name='Farrah', role='Thương nhân trái cây', desc='Đội xe bị Hilichurl tập kích sau khi một “quái nhân” từ trên trời rơi trúng doanh trại của chúng.')


# --- Chương II · Mở Đầu (Inazuma) ---
ATSUKO = dict(name='Atsuko', role='Người Inazuma sống ở cảng Liyue', desc='Người đã trốn khỏi Inazuma bằng chiếc bè nhỏ và được người Liyue cứu. Kể cho Lumine nghe về lệnh đóng cửa và chỉ cô đến tìm đội thuyền Nam Thập Tự.')
BEIDOU = dict(name='Beidou', role='Thủ lĩnh đội thuyền Nam Thập Tự', img='beidou_icon.png', desc='Chị đại hào sảng của chiếc thuyền “Ngôi Sao Chết Chóc”. Mời Lumine dự “Hội Đấu Võ Nam Thập Tự” và hứa tấm vé đến Inazuma cho người thắng.')
KAZUHA = dict(name='Kaedehara Kazuha', role='Ronin Samurai đến từ Inazuma', img='kazuha_icon.png', desc='Samurai phiêu bạt, nghe được “hơi thở” của gió và lá. Cung cấp chiếc Vision vô chủ làm giải thưởng và nhận ra Lumine dùng được nguyên tố mà không có Vision.')
ZHUHAN = dict(name='Zhuhan', role='Thuyền viên phụ trách báo danh', desc='Người ghi danh các tuyển thủ của Hội Đấu Võ và dẫn Lumine vào đấu trường qua từng vòng.')
CHUYUN = dict(name='Chú Yun', role='Tuyển thủ Hội Đấu Võ', desc='Á quân “Giải Đấu Võ Tự Do Ngật Hổ Nham”, kể về lần tay không bắt hai tên Đạo Bảo Đoàn.')
LINHSON = dict(name='Chai Yi và Liang', role='Truyền nhân “Phái Linh Sơn”', desc='Hai người trẻ luyện “Hóa Kình” và mong có Vision để làm sư phụ hài lòng.')
JINYOU = dict(name='Jinyou', role='Tuyển thủ tự nhận là “người hoàn hảo”', desc='Đối thủ đầu tiên của Lumine ở vòng dự tuyển.')
RONGSHI = dict(name='Rongshi', role='Đối thủ vòng bán kết', desc='Võ sĩ không muốn Vision, chỉ muốn tỷ võ để trưởng thành.')
FEI = dict(name='Fei', role='Đạo Bảo Đoàn, đối thủ chung kết', desc='Kẻ đã trộm chiếc Vision vô chủ nên không xuất hiện ở trận chung kết.')


SERIES = 'Genshin Impact · Light Novel'
FOOT = 'Truyện chuyển thể phi thương mại từ cốt truyện Genshin Impact (HoYoverse). Lời thoại theo bản tiếng Việt chính thức của game.'

# --- Chương II · Màn I (Inazuma) ---
BEIDOU_C2 = dict(name='Beidou', role='Thủ lĩnh đội thuyền Nam Thập Tự', img='beidou_icon.png', desc='Giữ lời hứa, đưa Lumine vượt qua giông bão đến Đảo Ritou trên thuyền “Ngôi Sao Chết Chóc”, rồi giao cô cho Thoma.')
THOMA = dict(name='Thoma', role='Người hầu của nhà Kamisato · Hiệp Hội Yashiro', img='thoma_icon.png', desc='Người đón Lumine ở Đảo Ritou, được Beidou giới thiệu là “thổ địa” và đối tác làm ăn. Bày ra những “khảo nghiệm” để xem cô có đủ sức “thay đổi thời cuộc” hay không.')
AYAKA = dict(name='Kamisato Ayaka', role='“Shirasagi Himegimi” · Đại tiểu thư Hiệp Hội Yashiro', img='ayaka_icon.png', desc='Người chống lại lệnh Truy Lùng Vision. Hứa tiến cử Lumine với Raiden Shogun nếu cô giúp ba người mất Vision.')
YOIMIYA = dict(name='Yoimiya', role='Chủ Tiệm Pháo Hoa Naganohara', img='yoimiya_icon.png', desc='“Nữ Hoàng Lễ Hội Hè” của Hanamizaka. Dùng Vision giả che mắt samurai và cùng Lumine lẻn vào Sở Trị An cứu sư phụ Masakatsu.')
SARA = dict(name='Kujou Sara', role='Đại tướng Quân Shogunate · Hiệp Hội Tenryou', img='sara_icon.png', desc='Con nuôi nhà Kujou, người thi hành lệnh Truy Lùng Vision. Trách phạt thuộc hạ dụng tư hình và tha cho nhóm Lumine đưa Masakatsu đi “chỉ lần này”.')
YAE = dict(name='Yae Miko', role='Đại pháp sư Đền Narukami', img='yae_icon.png', desc='“Yae đại nhân” có quan hệ thân thiết với Shogun. Chỉ ra căn bệnh của Domon và nói với Lumine rằng cô đến đúng thời cơ.')
CHISATO = dict(name='Hiiragi Chisato', role='Đại tiểu thư nhà Hiiragi · Hiệp Hội Kanjou', img='chisato_icon.png', desc='Nhờ Lumine đưa thư cho người thương Kujou Kamaji, đổi lại giúp cô trốn khỏi Đảo Ritou bằng đoàn hàng đi Đảo Watatsumi.')
SHINSUKE = dict(name='Hiiragi Shinsuke', role='Gia chủ nhà Hiiragi · Hiệp Hội Kanjou', desc='Tiếp đón Lumine niềm nở nhưng giao những việc vô lý để giữ chân cô lại Đảo Ritou.')
WERNER = dict(name='Werner', role='Thương nhân người Mondstadt kẹt ở Đảo Ritou', desc='Kẻ bán “Tủy Pha Lê” giá cao cho Keijirou. Nhớ quê, cuối cùng khai ra mưu đồ và dẫn Lumine đi tìm bằng chứng.')
KURISU = dict(name='Kurisu', role='Hội trưởng Thương Hội Vạn Quốc', desc='Thương nhân người Fontaine, bạn thân của Thoma, đang khốn đốn vì thuế “Tủy Pha Lê”.')
TEJIMA = dict(name='Tejima', role='Người canh giữ Làng Konda', img='tejima_icon.png', desc='Bảo vệ làng suốt 30 năm để chờ một người. Mất Vision và quên đi lý do mình ở lại.')
KUROSAWA = dict(name='Kurosawa Kyounosuke', role='Samurai Quân Shogunate', img='kurosawa_icon.png', desc='Tự bỏ tiền mua “lương thực cứu tế” cho dân, sau khi mất Vision thì quên hết và bị dân làng trách móc.')
DOMON = dict(name='Domon', role='Chưởng môn phái Meikyou Shisui', desc='Kiếm đạo gia muốn thành thiên hạ đệ nhất, phát điên sau khi mất Vision. Được sư huynh Anzai và các đệ tử giúp tỉnh lại.')
MASAKATSU = dict(name='Masakatsu', role='Nghệ nhân làm Vision giả', desc='Người làm Vision giả giúp Hiệp Hội Yashiro, bị Hiệp Hội Tenryou bắt giam ở Sở Trị An.')


# Mỗi màn: id (dùng làm tên thư mục web), arc (phần truyện), file nguồn, nhãn, tên, phụ đề, ảnh bìa, nhân vật, tên PDF, chân trang PDF, side=True nếu là nhiệm vụ bắt buộc (Màn X.1)
ACTS = [
  dict(id='man1', arc='Mở Đầu', src='man1.txt', act='Mở Đầu · Màn I', title='Người Phương Xa Đuổi Theo Gió', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='traveler_portrait.png', cast=[LUMINE, PAIMON, AETHER, GOD, AMBER, KAEYA, JEAN, LISA, DRAGON, BOY, VOICE],
       pdf='GenshinLN_MoDau_Man1_NguoiPhuongXaDuoiTheoGio.pdf', footer='Mở Đầu · Màn I — Người Phương Xa Đuổi Theo Gió', side=False),
  dict(id='man1-1', arc='Mở Đầu', src='man1_1.txt', act='Mở Đầu · Màn I.1', title='Ba Ngôi Đền Của Tứ Phong', sub='Nhiệm vụ bắt buộc để hoàn thành Màn I — Amber, Kaeya, Lisa',
       hero='lisa_splash.png', cast=[LUMINE, PAIMON, AMBER, KAEYA, LISA, JEAN, REDHAIR, MAGE, DVALIN],
       pdf='GenshinLN_MoDau_Man1.1_BaNgoiDenTuPhong.pdf', footer='Mở Đầu · Màn I.1 — Ba Ngôi Đền Của Tứ Phong', side=True),
  dict(id='man2', arc='Mở Đầu', src='man2.txt', act='Mở Đầu · Màn II', title='Vì Một Ngày Mai Không Rơi Lệ', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='venti_splash.png', cast=[LUMINE, PAIMON, VENTI, JEAN, DILUC, LISA, DVALIN2, MAGE2, ANASTASIA, GOTELINDE, SIGNORA],
       pdf='', footer='Mở Đầu · Màn II — Vì Một Ngày Mai Không Rơi Lệ', side=False),
  dict(id='man3', arc='Mở Đầu', src='man3.txt', act='Mở Đầu · Màn III', title='Bài Ca Về Rồng Và Tự Do', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='dvalin_wide.png', cast=[LUMINE, PAIMON, VENTI3, JEAN3, DILUC3, DVALIN3, MAGE3, AMBER3, KAEYA3, BARBARA, SIGNORA3],
       pdf='', footer='Mở Đầu · Màn III — Bài Ca Về Rồng Và Tự Do', side=False),
  dict(id='c1-man1', arc='Chương I · Liyue', src='c1_man1.txt', act='Chương I · Màn I', title='Phù Thế Phù Sinh Thiên Nham Gian', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='childe_card.png', cast=[LUMINE, PAIMON, CHILDE, NINGGUANG, REX, MOONCARVER, XIAO, GOLDET, YANXIAO, MING, MOUNTAIN, CLOUD, LIDING],
       pdf='', footer='Chương I · Màn I — Phù Thế Phù Sinh Thiên Nham Gian', side=False),
  dict(id='c1-man2', arc='Chương I · Liyue', src='c1_man2.txt', act='Chương I · Màn II', title='Lời Tạm Biệt Thể Xác Vĩnh Hằng', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='zhongli_card.png', cast=[LUMINE, PAIMON, ZHONGLI, CHILDE2, PING, QIQI, BAIZHU, GANYU, EKATERINA, SHITOU, YINGER],
       pdf='', footer='Chương I · Màn II — Lời Tạm Biệt Thể Xác Vĩnh Hằng', side=False),
  dict(id='c1-man3', arc='Chương I · Liyue', src='c1_man3.txt', act='Chương I · Màn III', title='Ngôi Sao Đang Đến', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='keqing_card.png', cast=[LUMINE, PAIMON, KEQING_C3, NINGGUANG_C3, GANYU_C3, ZHONGLI_C3, CHILDE_C3, SIGNORA_C3, XIAO_C3, ADEPTI_C3, PING_C3, OSIAL, MENGDAN],
       pdf='', footer='Chương I · Màn III — Ngôi Sao Đang Đến', side=False),
  dict(id='c1-man4-1', arc='Chương I · Liyue', src='c1_man4_1.txt', act='Chương I · Màn III.1', title='Ý Nghĩa Của Lupical', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương I · Màn IV — Chương Tiểu Lang - Màn I (Razor)',
       hero='razor_card.png', cast=[LUMINE, PAIMON, RAZOR41, AMBER41, BOREAS41, VILLAGERS41, DRAFF],
       pdf='', footer='Chương I · Màn III.1 — Ý Nghĩa Của Lupical', side=True),
  dict(id='c1-man4-2', arc='Chương I · Liyue', src='c1_man4_2.txt', act='Chương I · Màn III.2', title='Gió, Đôi Cánh Và Dũng Khí', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương I · Màn IV — Chương Tiểu Thố - Màn I (Amber)',
       hero='amber_splash.png', cast=[LUMINE, PAIMON, AMBER42, OTTO, RAPTOR, FARRAH],
       pdf='', footer='Chương I · Màn III.2 — Gió, Đôi Cánh Và Dũng Khí', side=True),
  dict(id='c1-man4-gt', arc='Chương I · Liyue', src='c1_man4_gt.txt', act='Chương I · Màn IV · Giới Thiệu', title='Dainsleif', sub='Nhiệm vụ mở đầu bắt buộc của Chương I · Màn IV — Người Giữ Cành',
       hero='dainsleif_banner.png', cast=[LUMINE, PAIMON, DAIN_GT, KATHERYNE, LAWRENCE, CHARLES],
       pdf='', footer='Chương I · Màn IV · Giới Thiệu — Dainsleif', side=True),
  dict(id='c1-man4', arc='Chương I · Liyue', src='c1_man4.txt', act='Chương I · Màn IV', title='Chúng Ta Ắt Sẽ Trùng Phùng', sub='Nhiệm vụ Ma Thần — Mondstadt và Liyue',
       hero='ganyu_card.png', cast=[LUMINE, PAIMON, DAIN4, GANYU4, LAN, HERALD, BARBARA4, ROSARIA, JEAN4, RAZOR, BOREAS, AETHER4],
       pdf='', footer='Chương I · Màn IV — Chúng Ta Ắt Sẽ Trùng Phùng', side=False),
  dict(id='c2-modau', arc='Chương II · Inazuma', src='c2_modau.txt', act='Chương II · Mở Đầu', title='Gió Thu Vén Áo Hỏi Lá Đỏ', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='kazuha_card.png', cast=[LUMINE, PAIMON, BEIDOU, KAZUHA, ATSUKO, ZHUHAN, CHUYUN, LINHSON, JINYOU, RONGSHI, FEI],
       pdf='', footer='Chương II · Mở Đầu — Gió Thu Vén Áo Hỏi Lá Đỏ', side=False),
  dict(id='c2-man1', arc='Chương II · Inazuma', src='c2_man1.txt', act='Chương II · Màn I', title='Lôi Thần Uy Nghiêm, Địa Đàng Vĩnh Hằng', sub='Nhiệm vụ Ma Thần — Inazuma',
       hero='ayaka_splash.png', cast=[LUMINE, PAIMON, THOMA, AYAKA, YOIMIYA, SARA, YAE, BEIDOU_C2, CHISATO, SHINSUKE, WERNER, KURISU, TEJIMA, KUROSAWA, DOMON, MASAKATSU],
       pdf='', footer='Chương II · Màn I — Lôi Thần Uy Nghiêm, Địa Đàng Vĩnh Hằng', side=False),
]