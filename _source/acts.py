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

# Chương II · Màn III
KOKOMI3 = dict(name='Sangonomiya Kokomi', role='Người Trị Vì Đảo Watatsumi · Thống soái quân kháng chiến', img='kokomi_icon.png', desc='Phong Lumine làm đội trưởng “Đội Cá Kiếm 2”. Khi phát hiện “vũ khí bí mật” của nhà tài trợ là Delusion của Fatui, cô ra lệnh tịch thu toàn bộ và chỉ cho Lumine nơi có thể là công xưởng.')
TEPPEI3 = dict(name='Teppei', role='Đội trưởng “Đội Cá Trích 1” · Quân kháng chiến', img='teppei_icon.png', desc='Người bạn đưa Lumine về Đảo Watatsumi. Lập nhiều chiến công nhờ “vũ khí bí mật” của nhà tài trợ, mà không biết đó là Delusion đang hút cạn sinh mạng mình.')
GOROU3 = dict(name='Gorou', role='Đại tướng quân kháng chiến', img='gorou_icon.png', desc='Phát hiện quân sĩ lão hóa kỳ lạ vì lén dùng “vũ khí bí mật”, mang một chiếc đến cho Kokomi. Dẫn quân kháng chiến xông lên trong trận chiến cuối cùng.')
OOKUBO = dict(name='Ookubo Daisuke', role='Quân kháng chiến · Đảo Watatsumi', desc='Người bàn chuyện quân lương với Kokomi, kể về nhà tài trợ giấu mặt.')
KOUTOKU = dict(name='Koutoku và Yoshihisa', role='Đội Cá Kiếm 2', desc='Đội trưởng đại diện và thành viên lão làng của Đội Cá Kiếm 2. Thử thách Lumine bằng đám ronin rồi công nhận cô làm đội trưởng.')
SCARA = dict(name='Scaramouche', role='Quan Chấp Hành thứ 6 của Fatui', img='scaramouche_icon.png', desc='Người “thay mặt thực hiện kế hoạch” ở công xưởng Delusion trên Đảo Yashiori. Khiêu khích Lumine bằng cái chết của Teppei và dùng oán niệm Ma Thần giăng bẫy cô.')
YAE3 = dict(name='Yae Miko', role='Guuji Đền Narukami · “Gia quyến” của Lôi Thần', img='yae_icon.png', desc='Cứu Lumine khỏi tay Scaramouche, kể về Ei và “Nhất Tâm Tịnh Thổ”, rồi vạch kế hoạch ly gián Hiệp Hội Tenryou để đưa Lumine trở lại trước mặt Raiden Shogun.')
SARA3 = dict(name='Kujou Sara', role='Đại tướng Quân Shogunate · Hiệp Hội Tenryou', img='sara_icon.png', desc='Đòi bắt Lumine ở Đền Narukami, nhận lời hẹn ba ngày của Yae Miko. Khi thấy chứng cứ, cô đối chất với gia chủ Kujou Takayuki và quyết định kháng lệnh.')
SAYU = dict(name='Sayu', role='Ninja của Shuumatsuban', img='sayu_icon.png', desc='Ninja hay buồn ngủ được Yae Miko “tóm” đến giúp. Lẻn vào Hiệp Hội Tenryou lấy công văn và thư từ trao đổi với Fatui.')
THOMA3 = dict(name='Thoma', role='Người hầu của nhà Kamisato · Hiệp Hội Yashiro', img='thoma_icon.png', desc='Vẫn trốn trong Phòng Trà Komore, nghĩ ra kế dùng pháo hoa của Yoimiya để dụ thân binh Hiệp Hội Tenryou.')
AYAKA3 = dict(name='Kamisato Ayaka', role='Đại tiểu thư nhà Kamisato', img='ayaka_icon.png', desc='Nhận ra công văn của Hiệp Hội Tenryou trình lên Shogun có vấn đề, cùng Lumine lập kế hoạch lấy chứng cứ.')
YOIMIYA3 = dict(name='Yoimiya', role='Chủ Tiệm Pháo Hoa Naganohara', img='yoimiya_icon.png', desc='Tặng Lumine một loại pháo hoa “siêu to khổng lồ” để dụ lính gác.')
TAKAYUKI = dict(name='Kujou Takayuki', role='Gia chủ nhà Kujou · Hiệp Hội Tenryou', img='takayuki_icon.png', desc='Thừa nhận đã qua lại với Fatui và che giấu chuyện tiền tuyến trong công văn trình lên Shogun, vì tin vào sức mạnh của “Lưỡi Đao Vô Tưởng”.')
SIGNORA3 = dict(name='Signora', role='Quan Chấp Hành thứ 8 của Fatui · Sứ giả Snezhnaya', img='signora_icon.png', desc='Kẻ giật dây chiến loạn ở Inazuma. Bị Lumine thách “Ngự Tiền Quyết Đấu” ở Thiên Thủ Các và thua trận.')
RAIDEN3 = dict(name='Raiden Shogun', role='Lôi Thần · Ei', img='raiden_icon.png', desc='Chứng kiến cuộc quyết đấu ở Thiên Thủ Các. Trong “Nhất Tâm Tịnh Thổ”, Ei bị nguyện vọng của người dân và Lumine đánh bại, rồi phế bỏ Lệnh Truy Lùng Vision.')
KAZUHA3 = dict(name='Kaedehara Kazuha', role='Ronin Samurai', img='kazuha_icon.png', desc='Xuất hiện trong trận chiến cuối cùng, đỡ lấy nhát “Lưỡi Đao Vô Tưởng”.')


# Mỗi màn: id (dùng làm tên thư mục web), arc (phần truyện), file nguồn, nhãn, tên, phụ đề, ảnh bìa, nhân vật, tên PDF, chân trang PDF, side=True nếu là nhiệm vụ bắt buộc (Màn X.1)
# --- Chương II · Màn I.1 (Kamisato Ayaka), Màn I.2 (Yoimiya), Màn II ---
AYAKA11 = dict(name='Kamisato Ayaka', role='“Shirasagi Himegimi” · Đại tiểu thư Hiệp Hội Yashiro', img='ayaka_icon.png', desc='Nhờ Lumine cùng chuẩn bị quà gặp mặt cho “Tsubaki”, cái tên lặp đi lặp lại trong sổ tay của người mẹ đã mất.')
OGURA = dict(name='Ogura Mio', role='Chủ Tiệm Vải Ogura', desc='Nhận may bộ kimono theo bản thiết kế của Ayaka, nhưng thiếu vải hoa nghê thường nhập từ Liyue.')
KURISU11 = dict(name='Kurisu', role='Hội trưởng Thương Hội Vạn Quốc', desc='Bị đám Ronin cướp mất lô vải cao cấp. Được Ayaka giúp lấy lại hàng.')
RONIN11 = dict(name='Ronin', role='Kẻ cướp hàng', desc='Cướp hàng của Thương Hội Vạn Quốc rồi đòi Kurisu bỏ tiền chuộc lại.')
KIMINAMI = dict(name='Kiminami Anna', role='Chủ Nhà Hàng Kiminami', desc='Quen biết anh em nhà Kamisato đã lâu, vui mừng khi thấy Ayaka dẫn bạn đến quán.')
FESTIVAL = dict(name='Sanden, Shimizu, Murakami, Yoshikawa', role='Chủ các sạp hàng ở lễ hội', desc='Nhiệt tình đón Ayaka đến lễ hội: tặng mặt nạ, mời rút quẻ, cho công thức bánh và bán thẻ cầu nguyện.')
YOIMIYA12 = dict(name='Yoimiya', role='Chủ Tiệm Pháo Hoa Naganohara', img='yoimiya_icon.png', desc='Bận rộn chuẩn bị “Hội Pháo Hoa Naganohara”, đồng thời tìm cách giúp kẻ vượt biên Sakujirou.')
KIDS12 = dict(name='Matsuzaka, Saika, Iwao', role='Lũ trẻ ở Đảo Narukami', desc='Muốn đánh đuổi “Siêu Mujina Youkai” bằng “vũ khí” chị Yoimiya chuẩn bị.')
RYUUNOSUKE = dict(name='Naganohara Ryuunosuke', role='Cha của Yoimiya', desc='Chủ cũ của Tiệm Pháo Hoa Naganohara, tai không còn nghe rõ nhưng luôn tươi cười và thích kể chuyện.')
SAKUJIROU = dict(name='Sakujirou', role='Kẻ vượt biên', desc='Người Inazuma đã bỏ đi, nay lén trở về và trốn trong Tiệm Pháo Hoa Naganohara.')
KOUICHI = dict(name='Kouichi', role='Bạn của Yoimiya', desc='Lén đóng thuyền để Sakujirou có đường rời Inazuma.')
MORIHIKO = dict(name='Morihiko', role='Khách quen của tiệm pháo hoa', desc='Chuẩn bị sẵn khoáng thạch làm pháo hoa cho Yoimiya.')
AMENOMA = dict(name='Amenoma Tougo và Hajime', role='Xưởng Rèn Amenoma', desc='Hai thầy trò thợ rèn. Amenoma Tougo đích thân gia công khoáng thạch cho Yoimiya.')
IMATANI = dict(name='Imatani Saburou và Imatani Kaori', role='Đôi vợ chồng già, khách cũ của tiệm pháo hoa', desc='Cha mẹ của Imatani Keisuke, sắp kỷ niệm 50 năm bên nhau.')
SATORU = dict(name='Satoru', role='Người dân Làng Konda', desc='Nhận Củ Cải Mặn do bà Kaori gửi đến.')
KEISUKE = dict(name='Imatani Keisuke', role='Hiệp Hội Tenryou', desc='Bạn thân thuở nhỏ của Sakujirou, nay là người dẫn quân truy bắt anh.')
YOSHITAKA = dict(name='Yoshitaka', role='Lính Hiệp Hội Tenryou', desc='Thuộc hạ của Keisuke, chặn đường nhóm Yoimiya.')
AYAKA2 = dict(name='Kamisato Ayaka', role='“Shirasagi Himegimi” · Đại tiểu thư Hiệp Hội Yashiro', img='ayaka_icon.png', desc='Báo tin Thoma bị Hiệp Hội Tenryou bắt đi làm “Vision thứ 100”.')
THOMA2 = dict(name='Thoma', role='Người hầu của nhà Kamisato · Hiệp Hội Yashiro', img='thoma_icon.png', desc='Bị bắt trong Nghi Thức Săn Vision. Cứu Lumine khỏi tay Raiden Shogun rồi chỉ cô đến Tatarasuna.')
RAIDEN = dict(name='Raiden Shogun', role='Vị thần cai trị Inazuma', img='raiden_icon.png', desc='Gọi Lumine là “ngoại lệ”, kẻ thù của sự vĩnh hằng, và đánh gục cô trong Nghi Thức Săn Vision.')
TEPPEI = dict(name='Teppei', role='Lính quân kháng chiến', img='teppei_icon.png', desc='Được Lumine cứu ở tiền tuyến, tiến cử cô với Gorou và dẫn cô đi khắp doanh trại.')
GOROU = dict(name='Gorou', role='Đại tướng quân kháng chiến', img='gorou_icon.png', desc='Thống lĩnh quân kháng chiến ở Tatarasuna. Nhận Lumine vào quân và không chịu giao cô cho Kujou Sara.')
SARA2 = dict(name='Kujou Sara', role='Đại tướng Quân Shogunate · Hiệp Hội Tenryou', img='sara_icon.png', desc='Dẫn viện binh đến tiền tuyến, đòi Gorou giao nộp Lumine và đề nghị “lâm trận quyết đấu”.')
KOKOMI = dict(name='Sangonomiya Kokomi', role='Thánh Pháp Sư của Đảo Watatsumi', img='kokomi_icon.png', desc='Người tổ chức quân kháng chiến. Đến Bờ Nazuchi cùng đội thuyền Nam Thập Tự, đẩy lui Quân Shogunate.')
KAZUHA2 = dict(name='Kaedehara Kazuha', role='Ronin Samurai · đội thuyền Nam Thập Tự', img='kazuha_icon.png', desc='Xuất hiện cùng Kokomi và đội thuyền Nam Thập Tự giữa trận chiến ở Bờ Nazuchi.')
BEIDOU2 = dict(name='Beidou', role='Thủ lĩnh đội thuyền Nam Thập Tự', img='beidou_icon.png', desc='Đưa “Ngôi Sao Chết Chóc” phục kích Quân Shogunate để hỗ trợ quân kháng chiến.')
RESIST = dict(name='Kaida Ryouma, Tokuda, Masashi, Shouji, Hisahiko', role='Người của quân kháng chiến', desc='Những người lính, thương binh và tân binh mà Lumine gặp trong doanh trại ở Tatarasuna.')

# --- Chương Đệm · Màn I ---
SHENHE = dict(name='Shenhe', role='Đệ tử của Lưu Vân Tá Phong Chân Quân', img='shenhe_icon.png', desc='Cô gái tóc trắng được Lumine giúp thoát khỏi đám lừa đảo ở Cảng Liyue. Lớn lên cùng tiên nhân nhưng là người phàm, mang Bùa Chú Tiên Gia đến cho Ningguang và giúp Lumine trong cuộc thi trùng tu Quần Ngọc Các.')
YUNJIN = dict(name='Yun Jin', role='Diễn viên nhạc kịch nổi tiếng của Liyue', img='yunjin_icon.png', desc='Đến tham gia cuộc thi để hỏi Ningguang về sân khấu cho vở kịch “Thần Nữ Hủy Diệt” của cha mình. Đề nghị nhóm Lumine và Beidou lập đội cùng giành ba suất đầu.')
XINGQIU = dict(name='Xingqiu', role='Nhị thiếu gia Thương Hội Phi Vân', img='xingqiu_icon.png', desc='Chỉ cho nhóm Lumine động tiên của Minh Hải Thê Hà Chân Quân ở gần Ngoại Ô Li Sa, nơi có thể có Minh Hà Phù Sinh Thạch.')
NINGGUANG_CD = dict(name='Ningguang', role='“Thiên Quyền” của Thất Tinh Liyue', img='ningguang_icon.png', desc='Tổ chức cuộc thi tìm nguyên liệu để trùng tu Quần Ngọc Các, đồng thời dùng việc này để dụ Beisht, kẻ đi theo Ma Thần Lốc Xoáy, ra khỏi mặt biển.')
BEIDOU_CD = dict(name='Beidou', role='Thủ lĩnh đội thuyền Nam Thập Tự', img='beidou_icon.png', desc='Mang đến một khối Minh Hà Phù Sinh Thạch, cùng Lumine và Yun Jin giành ba suất đầu của cuộc thi. Là người đã cảnh báo Ningguang về biến động dưới biển.')
CLOUD_CD = dict(name='Lưu Vân Tá Phong Chân Quân', role='Sư phụ của Shenhe', img='cloudretainer.png', desc='Kể cho Lumine và Paimon nghe quá khứ của Shenhe, nhờ họ chăm sóc con bé, và âm thầm quan sát xem Ningguang có vượt qua được phong ba sắp tới không.')
BAIZHU_CD = dict(name='Baizhu', role='Chủ Nhà Thuốc Bubu', img='baizhu_icon.png', desc='Cho nhóm Lumine biết về Minh Hà Phù Sinh Thạch trong “Thất Tàng Sơn Kinh” và gợi ý đến Thương Hội Phi Vân hỏi thăm.')
KEQING_CD = dict(name='Keqing', role='“Ngọc Hành Tinh” của Thất Tinh Liyue', img='keqing_icon.png', desc='Chỉ huy Thiên Nham Quân, ra lệnh cho máy Guizhong kiểu mới khai hỏa vào Beisht.')
BAIWEN = dict(name='Baiwen', role='Thư ký của Ningguang ở công trường', img='baiwen_icon.png', desc='Người nhận và chấm nguyên liệu của cuộc thi trùng tu Quần Ngọc Các.')
ZHANG = dict(name='Lão Zhang', role='Thợ rèn tiệm Hàn Phong Thiết Khí', img='zhang_icon.png', desc='Người từng làm Lõi Thần Kỳ cho Ningguang, chỉ cho nhóm Lumine đi tìm Quặng Sắt Sao Vỡ và Bí Hoa Thạch.')
MINGJUN = dict(name='Mingjun', role='Bạn thân của cha Shenhe', img='mingjun_icon.png', desc='Ông lão ở ngôi làng bỏ hoang gần Thiên Hoành Sơn, nơi Shenhe sinh ra. Nhiều năm vẫn day dứt vì đã không ngăn được cha của Shenhe.')
BEISHT = dict(name='Beisht', role='“Tàn Dư Lốc Xoáy”', img='beisht_icon.png', desc='Vợ của Osial, người cuối cùng đi theo Ma Thần Lốc Xoáy. Trồi lên từ biển khi Quần Ngọc Các bay lên.')
LIU = dict(name='Liu Mặt Sẹo và Qiang', role='Kẻ bán tình báo', desc='Hai gã lưu manh bám theo Shenhe đòi tiền, bị Thiên Nham Quân bắt đi.')

# --- Chương II · Màn IV ---
KATHERYNE_C2M4 = dict(name='Katheryne', role='Hiệp Hội Nhà Mạo Hiểm', desc='Giới thiệu cho Lumine ủy thác của người thợ mỏ Yuehui ở Vực Đá Sâu. Sáng hôm đó cô rút quẻ được lời dự báo về một “cuộc hội ngộ bất ngờ”.')
YUEHUI = dict(name='Yuehui', role='Thợ mỏ ở Vực Đá Sâu', img='yuehui_icon.png', desc='Một trong những thợ mỏ đầu tiên được cấp giấy phép khai thác Vực Đá Sâu. Ủy thác Lumine điều tra những Hilichurl chạy vào Vực Đá Sâu rồi không quay trở ra.')
DAIN_C2M4 = dict(name='Dainsleif', role='“Kiếm Sĩ Hoàng Hôn” · cựu đội trưởng đội cận vệ hoàng gia Khaenri\'ah', img='dainsleif_icon.png', desc='Đuổi theo một Sứ Đồ Vực Sâu qua cổng dịch chuyển và lạc đến Vực Đá Sâu, gặp lại Lumine. Cùng cô điều tra tòa thành đảo ngược, nơi có khả năng làm suy yếu lời nguyền.')
HALFDAN = dict(name='Halfdan', role='Kỵ Sĩ Hắc Xà', img='halfdan_icon.png', desc='Tinh anh trẻ tuổi trong đội cận vệ hoàng gia Khaenri\'ah năm xưa. Vẫn giữ được ý chí sau năm trăm năm, dẫn các Kỵ Sĩ Hắc Xà bảo vệ những Hilichurl đang chờ kết cục của mình.')
AETHER_C2M4 = dict(name='Aether', role='Anh trai song sinh của Lumine · “Hoàng tử điện hạ”', img='aether_icon.png', desc='Hiện ra trong ký ức mà Lumine thấy khi chạm vào hoa Inteyvat, đồng ý để Sứ Đồ Vực Sâu dùng “thiết bị” thanh tẩy lời nguyền.')
HERALD_C2M4 = dict(name='Sứ Đồ Vực Sâu', img='herald_icon.png', role='Giáo Đoàn Vực Sâu', desc='Kẻ từng bỏ chạy khỏi Dainsleif qua cổng dịch chuyển. Chặn đường nhóm Lumine để bảo vệ “ý chí của điện hạ” và bị đánh bại.')
LECTOR = dict(name='Linh Mục Vực Sâu', role='Giáo Đoàn Vực Sâu', desc='Canh giữ thiết bị khuếch đại ở căn phòng trung tâm của di tích, bị Lumine đánh bại.')
BSK = dict(name='Kỵ Sĩ Hắc Xà', role='Cựu cận vệ hoàng gia Khaenri\'ah', desc='Những kỵ sĩ mang lời nguyền canh giữ di tích và những Hilichurl già yếu. Theo Dainsleif, họ đang hô “mau chạy đi” bằng tiếng Khaenri\'ah cổ.')

# --- Chương Đệm · Màn I.1 (nhiệm vụ thế giới Vực Đá Sâu) ---
MUNING = dict(name='Muning', role='Chuyên viên Tổng Vụ ở Vực Đá Sâu', img='muning_icon.png', desc='Phụ trách doanh trại ở lối vào Vực Đá Sâu, cấp giấy phép cho những người muốn xuống hầm mỏ. Tính tình nóng nảy nhưng không phải người xấu.')
ZHIQIONG = dict(name='Zhiqiong', role='Nhà mạo hiểm · người thăm dò của đội thăm dò', img='zhiqiong_icon.png', desc='Nhà mạo hiểm trẻ hâm mộ Lumine, gọi cô là “tiền bối”. Chịu trách nhiệm tìm đường và vẽ bản đồ cho đội thăm dò Vực Đá Sâu.')
JINWU = dict(name='Jinwu', role='Kỹ thuật viên an ninh của đội thăm dò', img='jinwu_icon.png', desc='Sửa chữa và bảo trì thiết bị, đảm bảo an toàn cho cả đội. Luôn để mắt đến Zhiqiong.')
KHEDIVE = dict(name='Khedive', role='Học giả đến từ Sumeru', img='khedive_icon.png', desc='Người bỏ tiền thành lập và phụ trách đội thăm dò, nghiên cứu khoáng sản và sinh vật học.')
CLITOPHO = dict(name='Clitopho', role='Người bán “Thuốc Hảo Hán”', img='clitopho_icon.png', desc='Từng theo Đạo Bảo Đoàn, được Lumine cứu khỏi lồng giam rồi gia nhập đội thăm dò, giúp chế tạo đạn pháo.')

# --- Chương Đệm · Màn II ---
YELAN = dict(name='Yelan', role='Người tự xưng làm việc ở Tổng Vụ', img='yelan_icon.png', desc='Giám sát Vực Đá Sâu. Bí ẩn, quan sát tinh tường, đang điều tra chân tướng trận chiến với ma thú Khaenri\'ah năm trăm năm trước.')
YANFEI = dict(name='Yanfei', role='Cố vấn pháp lý nổi tiếng của Liyue', img='yanfei_icon.png', desc='Mang huyết thống tiên thú. Đến Vực Đá Sâu để thực hiện một bản di chúc: tìm lại pháp bảo La Bàn Huyền Ảo.')
ITTO = dict(name='Arataki Itto', role='Đại ca Bang Arataki', img='itto_icon.png', desc='Người Inazuma đến Liyue cùng Shinobu. Được Yanfei giúp thoát khỏi đại lao Liyue, nên bám theo để “báo ơn”.')
SHINOBU = dict(name='Kuki Shinobu', role='Thành viên Bang Arataki', img='shinobu_icon.png', desc='Người lo liệu mọi việc trong Bang Arataki. Từng học luật ở Liyue, đến lấy bằng tốt nghiệp.')
USHI = dict(name='Ushi', role='Thành viên ngoài biên chế của Bang Arataki', desc='Chú bò của Itto, giỏi tìm đường. Chỉ nói “Moo”, nhưng Itto hiểu hết.')
XIAO_CD2 = dict(name='Xiao', role='Hộ Pháp Dạ Xoa · Hàng Ma Đại Thánh', img='xiao_icon.png', desc='Một mình đến Vực Đá Sâu tìm tung tích của một Dạ Xoa đã mất tích.')
FUSHE = dict(name='Phù Xá', role='Đằng Xà Thái Nguyên Soái · Dạ Xoa', img='bosacius_icon.png', desc='Người đứng đầu trong năm Dạ Xoa dưới trướng Nham Vương Đế Quân, đã mất tích hàng trăm năm. Xiao đến Vực Đá Sâu để tìm anh.')
BOYANG = dict(name='Boyang', role='Thuật sĩ · tổ tiên của Yelan', desc='Một trong các tổ tiên của Yelan, người năm xưa đến Vực Đá Sâu và không thể trở về.')
ZHONGLI_CD2 = dict(name='Zhongli', role='Khách của Vãng Sinh Đường', img='zhongli_icon.png', desc='Lặng lẽ dõi theo từ trên vách núi.')

# --- Chương III · Màn I (Sumeru) ---
TIGHNARI = dict(name='Tighnari', role='Đội Trưởng Kiểm Lâm · Làng Gandharva', img='tighnari_icon.png', desc='Người thầy của Collei, am hiểu thực vật và bào chế thuốc. Đã nhiều lần từ chối lời mời nhậm chức của Giáo Viện, cùng Lumine đi giải quyết Tử Vực và tìm cách cứu Haypasia.')
COLLEI = dict(name='Collei', role='Kiểm lâm tập sự · Làng Gandharva', img='collei_icon.png', desc='Học trò của Tighnari, bạn thư từ của Amber ở Mondstadt. Đã đưa Lumine ngất xỉu về làng; từ nhỏ mắc bệnh Eleazar nên phải hạn chế chạm vào đồ vật.')
KIEMLAM = dict(name='Amir và Nasrin', role='Nhân viên kiểm lâm · Làng Gandharva', desc='Hai nhân viên kiểm lâm của làng, thường nói chuyện với Tighnari về việc tuần tra, nấm độc và Tử Vực.')
HAYPASIA = dict(name='Haypasia', role='Học giả Học Phái Rtawahist · Giáo Viện', img='haypasia_icon.png', desc='Học giả ẩn cư trong hang núi, dùng Linh Phân Hương để thiền định và kết nối với Cây Thế Giới. Lumine ngất đi vì làn khói hương của cô.')
HERALD_C3 = dict(name='Sứ Đồ Vực Sâu', role='Giáo Đoàn Vực Sâu', img='herald_icon.png', desc='Xuất hiện trong giấc mơ của Lumine ở hang núi, nói rằng “Hoàng tử đại nhân” đã bỏ rơi cô và hành trình tìm anh vốn đã không còn ý nghĩa.')
GIAOVIEN = dict(name='Ghulam và Khajeh', role='Người của Giáo Viện', desc='Hai người của Giáo Viện đến Làng Gandharva để mời Tighnari về Thành Sumeru, bị Tighnari từ chối.')
PANAH = dict(name='Panah, Rohawi và Asfand', role='Giáo Viện · Lữ Đoàn 30', desc='Panah trao Trạm Cuối Akasha cho khách mới đến Thành Sumeru, Rohawi là nhà nghiên cứu quen biết Tighnari, Asfand là cố vấn của Lữ Đoàn 30, nhóm Eremite phụ trách an ninh thành.')
DUNYARZAD = dict(name='Dunyarzad', role='Tiểu thư nhà Homayani', img='dunyarzad_icon.png', desc='Tín đồ trung thành của Tiểu Vương Kusanali, đang chuẩn bị Lễ Hội Sabzeruz. Cho Lumine biết Tiểu Vương Kusanali thật sự được người dân yêu mến.')
DEHYA = dict(name='Dehya', role='Eremite · Vệ sĩ của Dunyarzad', img='dehya_icon.png', desc='Vệ sĩ của Dunyarzad, mạnh mẽ và thẳng tính, luôn theo sát tiểu thư để bảo vệ cô.')
NILOU = dict(name='Nilou', role='Vũ công · Đại Khu Bazaar', img='nilou_icon.png', desc='Vũ công đang cùng mọi người trang trí Đại Khu Bazaar và chuẩn bị điệu múa cho Lễ Hội Sabzeruz, mời Lumine đừng bỏ lỡ lễ hội.')
ALHAITHAM = dict(name='Alhaitham', role='Học giả · Giáo Viện', img='alhaitham_icon.png', desc='Học giả của Giáo Viện, muốn nghiên cứu “Hũ Tri Thức Thần”. Cùng Lumine truy tìm nó ở Cảng Ormos, rồi giao đấu với nhóm Ayn Al-Ahmar.')
DORI = dict(name='Dori', role='Thương nhân bách hóa · Cảng Ormos', img='dori_icon.png', desc='Thương nhân mê Mora ở Cảng Ormos, bán đủ thứ hàng và tình báo. Giúp Lumine tìm ra manh mối về Hũ Tri Thức Thần.')
AYN = dict(name='Tariq và Tumart', role='Nhóm Eremite Ayn Al-Ahmar', desc='Thành viên của Ayn Al-Ahmar, những người tôn thờ Vua Deshret và giữ trong tay “Hũ Tri Thức Thần”.')
GIAOVIEN2 = dict(name='Học sinh Giáo Viện và người dân Sumeru', role='Những người khác', desc='Các học sinh và người dân Thành Sumeru, Cảng Ormos gặp trên đường đi: Lambad, Muruwa, Hamasa, Sharaf, Aftab, Kumari, Shrimati, Farhad, Rama, Pooria, Jayant, Elham, Sidhu, Bandi, Kudari, Eymen, Latish, Raunak.')
KATHERYNE_C3 = dict(name='Katheryne', role='Hiệp Hội Nhà Mạo Hiểm · Thành Sumeru', desc='Nhân viên hiệp hội tại Thành Sumeru, cho Lumine biết thêm tình hình và chỉ đường.')

# --- Chương III · Màn II (Sumeru) ---
DUNYARZAD2 = dict(name='Dunyarzad', role='Tiểu thư nhà Homayani · người tổ chức Lễ Hội Sabzeruz', img='dunyarzad_icon.png', desc='Tiết lộ mình mắc bệnh Eleazar giai đoạn cuối, vẫn dốc sức tổ chức Lễ Hội Sabzeruz để mừng sinh nhật Tiểu Vương Kusanali, và là người cùng Lumine bị cuốn vào vòng “samsara”.')
DEHYA2 = dict(name='Dehya', role='Eremite · Vệ sĩ của Dunyarzad', img='dehya_icon.png', desc='Bảo vệ Dunyarzad và buổi lễ, cùng Lumine đối đầu Eremite định bắt cóc cô, rồi bị cuốn vào việc chứng minh “cọc gỗ” trong vòng lặp ngày lễ.')
NILOU2 = dict(name='Nilou', role='Vũ công · Đại Khu Bazaar', img='nilou_icon.png', desc='Chuẩn bị biểu diễn Vũ Điệu Sabzeruz, bị Giáo Viện cấm; cuối cùng điệu múa vẫn diễn ra với hai chậu Padisarah.')
NAHIDA = dict(name='Nahida', role='Cô gái bí ẩn', img='nahida_icon.png', desc='Cô gái nhỏ nhắn chỉ vài người nhìn thấy, tự xưng là “mặt trăng” và nhắc Lumine rằng họ đang bị nhốt trong một “samsara”. Cuối màn, Lumine nhận ra cô là Tiểu Vương Kusanali.')
KIMIYA = dict(name='Kimiya', role='Người bán “Bói Giả Kim”', img='kimiya_icon.png', desc='Bày quầy “Bói Giả Kim” trong lễ hội, dùng nguyên liệu của khách để luyện kim rồi đoán ý nghĩa từ kết quả.')
VIHAR = dict(name='Vihar', role='Người đóng “Kỵ Sĩ Hoa Farris”', img='vihar_icon.png', desc='Phát Kẹo Yalda cho trẻ em trong lễ hội, tự xưng “Kỵ Sĩ Hoa Farris” và rất quý Dunyarzad.')
AZAR = dict(name='Azar', role='Đại Hiền Giả · Giáo Viện', img='azar_icon.png', desc='Ra lệnh dỡ bỏ Vũ Điệu Sabzeruz và cấm lễ hội, cho rằng tự ý tổ chức lễ hội của thần là vi phạm lệnh cấm.')
SETARIA = dict(name='Setaria', role='Người của Giáo Viện', desc='Đi cùng Azar, đọc lệnh cấm tổ chức Lễ Hội Sabzeruz.')
BADIS = dict(name='Badis và Idder', role='Eremite', desc='Hai Eremite định bắt cóc Dunyarzad trong lễ hội.')
AMAL = dict(name='Amal và Lambad', role='Chủ quầy · Chủ quán rượu', desc='Amal bán “Bàn Tiệc Haft-Mewa” trong lễ hội, Lambad là chủ Quán Rượu Lambad.')
OTHERS_C32 = dict(name='Người dân Thành Sumeru', role='Những người khác', desc='Bọn trẻ trong lễ hội, vệ binh và thương nhân ở cổng thành, một người lạ xuất hiện ở cuối màn.')

# --- Chương III · Màn II · Kết và Màn III (Sumeru) ---
NAHIDA_K = dict(name='Nahida', role='Tiểu Vương Kusanali · Thảo Thần', img='nahida_icon.png', desc='Nói chuyện với Lumine qua thân thể của Katheryne, kể về vị trí của mình ở Thánh Địa Surasthana và nhờ hai người cùng điều tra các hiền giả.')
KATHERYNE_K = dict(name='Katheryne', role='Hiệp Hội Nhà Mạo Hiểm · Thành Sumeru', img='katheryne_icon.png', desc='Nhân viên của hiệp hội, thân thể mà Nahida mượn ý thức để nói chuyện với Lumine. Chỉ nói chuyện thật của mình ở cuối phần.')
DUNYARZAD_K = dict(name='Dunyarzad', role='Tiểu thư nhà Homayani', img='dunyarzad_icon.png', desc='Vừa thoát khỏi vòng “samsara” và tỉnh lại sau giấc mơ về Vũ Điệu Sabzeruz.')
NILOU_K = dict(name='Nilou', role='Vũ công · Đại Khu Bazaar', img='nilou_icon.png', desc='Chỉ xuất hiện trong đoạn phim mở đầu, bước ra sân khấu dâng lên Vũ Điệu Sabzeruz.')
NAHIDA3 = dict(name='Nahida', role='Tiểu Vương Kusanali · Thảo Thần', img='nahida_icon.png', desc='Vẫn nói chuyện qua thân thể Katheryne, cùng Lumine và Paimon điều tra các hiền giả, nhờ Setaria giúp và cuối cùng rút lui vào ý thức khi bị Dottore phát hiện.')
KATHERYNE3 = dict(name='Katheryne', role='Hiệp Hội Nhà Mạo Hiểm · Thành Sumeru', img='katheryne_icon.png', desc='Nhân viên hiệp hội, thân thể mà Nahida mượn ý thức trong màn này.')
SETARIA3 = dict(name='Setaria', role='Học giả Giáo Viện · Trợ lý của Azar', img='setaria_icon.png', desc='Học giả xuất thân từ sa mạc, được Nahida chọn để giúp, bị Lumine, Paimon và Nahida thuyết phục trong cuộc điều tra các hiền giả.')
QUENSETARIA = dict(name='Nabiya, Akim, Qishan và Rima', role='Người quen của Setaria · Lữ Đoàn 30', desc='Thầy bói Nabiya, thợ gốm Akim, nữ học viên Qishan và lính đánh thuê Rima của Lữ Đoàn 30; bốn người bị Dottore dùng Trạm Cuối Akasha cải tiến để “truy cập” ý thức.')
DOTTORE = dict(name='Dottore', role='Quan Chấp Hành Fatui thứ hai', img='dottore_icon.png', desc='Từng là người bị Giáo Viện trục xuất, tự xưng là “Dottore”. Cải tiến Trạm Cuối Akasha để đưa thông tin vào tiềm thức dân chúng, và phát hiện ý thức mạnh mẽ của Nahida.')
TIGHNARI3 = dict(name='Tighnari', role='Đội Trưởng Kiểm Lâm · Làng Gandharva', img='tighnari_icon.png', desc='Cùng Lumine và Paimon tìm manh mối về Haypasia ở Pardis Dhyai.')
COLLEI3 = dict(name='Collei', role='Kiểm lâm tập sự · Làng Gandharva', img='collei_icon.png', desc='Học trò của Tighnari, đi cùng thầy trong cuộc tìm kiếm.')
HAYPASIA3 = dict(name='Haypasia', role='Học giả Học Phái Rtawahist · Giáo Viện', img='haypasia_icon.png', desc='Học giả đã kết nối với “ý thức thần linh” và cho Lumine thấy một cảnh qua ý thức đó.')
ALHAITHAM3 = dict(name='Alhaitham', role='Quan Thư Ký · Giáo Viện', img='alhaitham_icon.png', desc='Cùng Lumine đối mặt Cyno ở sa mạc, giấu “Hũ Tri Thức Thần” trên người.')
CYNO = dict(name='Cyno', role='Tổng Quản Mahamatra · tự trục xuất', img='cyno_icon.png', desc='Cấp trên của các Matra trong Giáo Viện, nay đã “tự trục xuất” và đơn độc đến sa mạc, đòi Alhaitham giao ra “Hũ Tri Thức Thần”.')
DEHYA3 = dict(name='Dehya', role='Eremite · “Sư Tử Lửa”', img='dehya_icon.png', desc='Xuất hiện ở sa mạc trong lúc Lumine và nhóm bị cuốn vào bão cát.')
CANDACE = dict(name='Candace', role='Hộ vệ Làng Aaru', img='candace_icon.png', desc='Hộ vệ của Làng Aaru, dẫn mọi người đến nhà trưởng làng để tránh bão cát và nhận lời giúp đỡ.')
ISAK = dict(name='Isak', role='Cậu bé tìm ông nội', img='isak_icon.png', desc='Cậu bé xin được đi cùng Lumine để tìm ông nội đã mất tích, nhất quyết ông không phải người xấu.')
ANPU = dict(name='Chú Anpu', role='Trưởng làng Aaru', desc='Trưởng Làng Aaru, kể về bão cát ngày càng nghiêm trọng quanh làng.')
OTHERS_C33 = dict(name='Người dân và lính đánh thuê', role='Những người khác', desc='Lính đánh thuê mai phục, thành viên Eremite theo dõi, người dân Thành Sumeru và giọng nói trong ý thức của Haypasia.')

ACTS = [
  dict(id='man1', arc='Mở Đầu', src='man1.txt', act='Mở Đầu · Màn I', title='Người Phương Xa Đuổi Theo Gió', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='sc_man1.jpg', cast=[LUMINE, PAIMON, AETHER, GOD, AMBER, KAEYA, JEAN, LISA, DRAGON, BOY, VOICE],
       pdf='GenshinLN_MoDau_Man1_NguoiPhuongXaDuoiTheoGio.pdf', footer='Mở Đầu · Màn I — Người Phương Xa Đuổi Theo Gió', side=False),
  dict(id='man1-1', arc='Mở Đầu', src='man1_1.txt', act='Mở Đầu · Màn I.1', title='Ba Ngôi Đền Của Tứ Phong', sub='Nhiệm vụ bắt buộc để hoàn thành Màn I — Amber, Kaeya, Lisa',
       hero='sc_man1_1.jpg', thumb='sc_man1_1.jpg', cast=[LUMINE, PAIMON, AMBER, KAEYA, LISA, JEAN, REDHAIR, MAGE, DVALIN],
       pdf='GenshinLN_MoDau_Man1.1_BaNgoiDenTuPhong.pdf', footer='Mở Đầu · Màn I.1 — Ba Ngôi Đền Của Tứ Phong', side=True),
  dict(id='man2', arc='Mở Đầu', src='man2.txt', act='Mở Đầu · Màn II', title='Vì Một Ngày Mai Không Rơi Lệ', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='sc_man2.jpg', cast=[LUMINE, PAIMON, VENTI, JEAN, DILUC, LISA, DVALIN2, MAGE2, ANASTASIA, GOTELINDE, SIGNORA],
       pdf='', footer='Mở Đầu · Màn II — Vì Một Ngày Mai Không Rơi Lệ', side=False),
  dict(id='man3', arc='Mở Đầu', src='man3.txt', act='Mở Đầu · Màn III', title='Bài Ca Về Rồng Và Tự Do', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='dvalin_wide.png', cast=[LUMINE, PAIMON, VENTI3, JEAN3, DILUC3, DVALIN3, MAGE3, AMBER3, KAEYA3, BARBARA, SIGNORA3],
       pdf='', footer='Mở Đầu · Màn III — Bài Ca Về Rồng Và Tự Do', side=False),
  dict(id='c1-man1', arc='Chương I · Liyue', src='c1_man1.txt', act='Chương I · Màn I', title='Phù Thế Phù Sinh Thiên Nham Gian', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='sc_c1_man1.jpg', cast=[LUMINE, PAIMON, CHILDE, NINGGUANG, REX, MOONCARVER, XIAO, GOLDET, YANXIAO, MING, MOUNTAIN, CLOUD, LIDING],
       pdf='', footer='Chương I · Màn I — Phù Thế Phù Sinh Thiên Nham Gian', side=False),
  dict(id='c1-man2', arc='Chương I · Liyue', src='c1_man2.txt', act='Chương I · Màn II', title='Lời Tạm Biệt Thể Xác Vĩnh Hằng', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='sc_c1_man2.jpg', cast=[LUMINE, PAIMON, ZHONGLI, CHILDE2, PING, QIQI, BAIZHU, GANYU, EKATERINA, SHITOU, YINGER],
       pdf='', footer='Chương I · Màn II — Lời Tạm Biệt Thể Xác Vĩnh Hằng', side=False),
  dict(id='c1-man3', arc='Chương I · Liyue', src='c1_man3.txt', act='Chương I · Màn III', title='Ngôi Sao Đang Đến', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='sc_c1_man3.jpg', cast=[LUMINE, PAIMON, KEQING_C3, NINGGUANG_C3, GANYU_C3, ZHONGLI_C3, CHILDE_C3, SIGNORA_C3, XIAO_C3, ADEPTI_C3, PING_C3, OSIAL, MENGDAN],
       pdf='', footer='Chương I · Màn III — Ngôi Sao Đang Đến', side=False),
  dict(id='c1-man4-1', arc='Chương I · Liyue', src='c1_man4_1.txt', act='Chương I · Màn III.1', title='Ý Nghĩa Của Lupical', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương I · Màn IV — Chương Tiểu Lang - Màn I (Razor)',
       hero='sc_c1_man4_1.jpg', thumb='sc_c1_man4_1.jpg', cast=[LUMINE, PAIMON, RAZOR41, AMBER41, BOREAS41, VILLAGERS41, DRAFF],
       pdf='', footer='Chương I · Màn III.1 — Ý Nghĩa Của Lupical', side=True),
  dict(id='c1-man4-2', arc='Chương I · Liyue', src='c1_man4_2.txt', act='Chương I · Màn III.2', title='Gió, Đôi Cánh Và Dũng Khí', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương I · Màn IV — Chương Tiểu Thố - Màn I (Amber)',
       hero='sc_c1_man4_2.jpg', thumb='sc_c1_man4_2.jpg', cast=[LUMINE, PAIMON, AMBER42, OTTO, RAPTOR, FARRAH],
       pdf='', footer='Chương I · Màn III.2 — Gió, Đôi Cánh Và Dũng Khí', side=True),
  dict(id='c1-man4-gt', arc='Chương I · Liyue', src='c1_man4_gt.txt', act='Chương I · Màn IV · Giới Thiệu', title='Dainsleif', sub='Nhiệm vụ mở đầu bắt buộc của Chương I · Màn IV — Người Giữ Cành',
       hero='dainsleif_banner.png', thumb='dainsleif_thumb.png', cast=[LUMINE, PAIMON, DAIN_GT, KATHERYNE, LAWRENCE, CHARLES],
       pdf='', footer='Chương I · Màn IV · Giới Thiệu — Dainsleif', side=True),
  dict(id='c1-man4', arc='Chương I · Liyue', src='c1_man4.txt', act='Chương I · Màn IV', title='Chúng Ta Ắt Sẽ Trùng Phùng', sub='Nhiệm vụ Ma Thần — Mondstadt và Liyue',
       hero='sc_c1_man4.jpg', cast=[LUMINE, PAIMON, DAIN4, GANYU4, LAN, HERALD, BARBARA4, ROSARIA, JEAN4, RAZOR, BOREAS, AETHER4],
       pdf='', footer='Chương I · Màn IV — Chúng Ta Ắt Sẽ Trùng Phùng', side=False),
  dict(id='c2-modau', arc='Chương II · Inazuma', src='c2_modau.txt', act='Chương II · Mở Đầu', title='Gió Thu Vén Áo Hỏi Lá Đỏ', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='sc_c2_modau.jpg', cast=[LUMINE, PAIMON, BEIDOU, KAZUHA, ATSUKO, ZHUHAN, CHUYUN, LINHSON, JINYOU, RONGSHI, FEI],
       pdf='', footer='Chương II · Mở Đầu — Gió Thu Vén Áo Hỏi Lá Đỏ', side=False),
  dict(id='c2-man1', arc='Chương II · Inazuma', src='c2_man1.txt', act='Chương II · Màn I', title='Lôi Thần Uy Nghiêm, Địa Đàng Vĩnh Hằng', sub='Nhiệm vụ Ma Thần — Inazuma',
       hero='sc_c2_man1.jpg', cast=[LUMINE, PAIMON, THOMA, AYAKA, YOIMIYA, SARA, YAE, BEIDOU_C2, CHISATO, SHINSUKE, WERNER, KURISU, TEJIMA, KUROSAWA, DOMON, MASAKATSU],
       pdf='', footer='Chương II · Màn I — Lôi Thần Uy Nghiêm, Địa Đàng Vĩnh Hằng', side=False),
  dict(id='c2-man1-1', arc='Chương II · Inazuma', src='c2_man1_1.txt', act='Chương II · Màn I.1', title='Câu Chuyện Về Hạc Và Thỏ Trắng', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương II · Màn II — Chương Tuyết Hạc - Màn I (Kamisato Ayaka)',
       hero='sc_c2_man1_1.jpg', thumb='sc_c2_man1_1.jpg', cast=[LUMINE, PAIMON, AYAKA11, OGURA, KURISU11, RONIN11, KIMINAMI, FESTIVAL],
       pdf='', footer='Chương II · Màn I.1 — Câu Chuyện Về Hạc Và Thỏ Trắng', side=True),
  dict(id='c2-man1-2', arc='Chương II · Inazuma', src='c2_man1_2.txt', act='Chương II · Màn I.2', title='Vĩnh hằng như một giấc mơ', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương II · Màn II — Chương Lưu Kim - Màn I (Yoimiya)',
       hero='sc_c2_man1_2.jpg', thumb='sc_c2_man1_2.jpg', cast=[LUMINE, PAIMON, YOIMIYA12, KIDS12, RYUUNOSUKE, SAKUJIROU, KOUICHI, MORIHIKO, AMENOMA, IMATANI, SATORU, KEISUKE, YOSHITAKA],
       pdf='', footer='Chương II · Màn I.2 — Vĩnh hằng như một giấc mơ', side=True),
  dict(id='c2-man2', arc='Chương II · Inazuma', src='c2_man2.txt', act='Chương II · Màn II', title='Tâm Vô Tạp Niệm, Bất Sinh Bất Diệt', sub='Nhiệm vụ Ma Thần — Inazuma',
       hero='sc_c2_man2.jpg', cast=[LUMINE, PAIMON, AYAKA2, THOMA2, RAIDEN, TEPPEI, GOROU, SARA2, KOKOMI, KAZUHA2, BEIDOU2, RESIST],
       pdf='', footer='Chương II · Màn II — Tâm Vô Tạp Niệm, Bất Sinh Bất Diệt', side=False),
  dict(id='c2-man3', arc='Chương II · Inazuma', src='c2_man3.txt', act='Chương II · Màn III', title='Thiên Thủ Bách Nhãn, Thiên Hạ Nhân Gian', sub='Nhiệm vụ Ma Thần — Inazuma',
       hero='raiden_nc.png', cast=[LUMINE, PAIMON, KOKOMI3, TEPPEI3, GOROU3, OOKUBO, KOUTOKU, SCARA, YAE3, SARA3, SAYU, THOMA3, AYAKA3, YOIMIYA3, TAKAYUKI, SIGNORA3, RAIDEN3, KAZUHA3],
       pdf='', footer='Chương II · Màn III — Thiên Thủ Bách Nhãn, Thiên Hạ Nhân Gian', side=False),
  dict(id='cd-man1', arc='Chương II · Inazuma', src='cd_man1.txt', act='Chương Đệm · Màn I', title='Phong Khởi Hạc Quy', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='sc_cd_man1.jpg', cast=[LUMINE, PAIMON, SHENHE, YUNJIN, NINGGUANG_CD, BEIDOU_CD, CLOUD_CD, XINGQIU, BAIZHU_CD, KEQING_CD, BAIWEN, ZHANG, MINGJUN, BEISHT, LIU],
       pdf='', footer='Chương Đệm · Màn I — Phong Khởi Hạc Quy', side=False),
  dict(id='c2-man4', arc='Chương II · Inazuma', src='c2_man4.txt', act='Chương II · Màn IV', title='Khúc An Hồn Nơi Đáy Vực', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='sc_c2_man4.jpg', cast=[LUMINE, PAIMON, DAIN_C2M4, HALFDAN, AETHER_C2M4, KATHERYNE_C2M4, YUEHUI, HERALD_C2M4, LECTOR, BSK],
       pdf='', footer='Chương II · Màn IV — Khúc An Hồn Nơi Đáy Vực', side=False),
  dict(id='cd-man1-1', arc='Chương II · Inazuma', src='cd_man1_1.txt', act='Chương Đệm · Màn I.1', title='Hành Trình Bên Trong Vực Đá Sâu', sub='Nhiệm vụ thế giới bắt buộc để mở Chương Đệm · Màn II — Vực Đá Sâu, Liyue',
       hero='chasm.png', cast=[LUMINE, PAIMON, ZHIQIONG, MUNING, JINWU, KHEDIVE, CLITOPHO],
       pdf='', footer='Chương Đệm · Màn I.1 — Hành Trình Bên Trong Vực Đá Sâu', side=True),
  dict(id='cd-man2', arc='Chương II · Inazuma', src='cd_man2.txt', act='Chương Đệm · Màn II', title='Lộ Trình Nguy Hiểm', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='sc_cd_man2.jpg', cast=[LUMINE, PAIMON, YELAN, YANFEI, ITTO, SHINOBU, USHI, XIAO_CD2, FUSHE, BOYANG, ZHONGLI_CD2],
       pdf='', footer='Chương Đệm · Màn II — Lộ Trình Nguy Hiểm', side=False),
  dict(id='c3-man1', arc='Chương III · Sumeru', src='c3_man1.txt', act='Chương III · Màn I', title='Xuyên Qua Màn Sương Và Rừng Rậm', sub='Nhiệm vụ Ma Thần — Sumeru',
       hero='sc_c3_man1.jpg', cast=[LUMINE, PAIMON, TIGHNARI, COLLEI, KIEMLAM, HAYPASIA, HERALD_C3, GIAOVIEN, PANAH, KATHERYNE_C3, DUNYARZAD, DEHYA, NILOU, ALHAITHAM, DORI, AYN, GIAOVIEN2],
       pdf='', footer='Chương III · Màn I — Xuyên Qua Màn Sương Và Rừng Rậm', side=False),
  dict(id='c3-man2', arc='Chương III · Sumeru', src='c3_man2.txt', act='Chương III · Màn II', title='Bình Minh Của Ngàn Đóa Hồng', sub='Nhiệm vụ Ma Thần — Sumeru',
       hero='c3m2_q2.png', cast=[LUMINE, PAIMON, DUNYARZAD2, DEHYA2, NILOU2, NAHIDA, KIMIYA, VIHAR, AZAR, SETARIA, BADIS, AMAL, OTHERS_C32],
       pdf='', footer='Chương III · Màn II — Bình Minh Của Ngàn Đóa Hồng', side=False),
  dict(id='c3-man2-ket', arc='Chương III · Sumeru', src='c3_man2_ket.txt', act='Chương III · Màn II · Kết', title='Bình Minh Của Ngàn Đóa Hồng - Kết', sub='Phần cuối của Chương III · Màn II — nhiệm vụ “Bình Minh” (Chương 3 Màn 2 - Kết)',
       hero='c3m2k_q1.png', cast=[LUMINE, PAIMON, NAHIDA_K, KATHERYNE_K, DUNYARZAD_K, NILOU_K],
       pdf='', footer='Chương III · Màn II · Kết — Bình Minh Của Ngàn Đóa Hồng - Kết', side=False),
  dict(id='c3-man3', arc='Chương III · Sumeru', src='c3_man3.txt', act='Chương III · Màn III', title='Ảo Mộng, Trống Rỗng Và Dối Gian', sub='Nhiệm vụ Ma Thần — Sumeru',
       hero='sc_c3_man3.jpg', cast=[LUMINE, PAIMON, NAHIDA3, KATHERYNE3, SETARIA3, QUENSETARIA, DOTTORE, TIGHNARI3, COLLEI3, HAYPASIA3, ALHAITHAM3, CYNO, DEHYA3, CANDACE, ISAK, ANPU, OTHERS_C33],
       pdf='', footer='Chương III · Màn III — Ảo Mộng, Trống Rỗng Và Dối Gian', side=False),

  # === Các Màn Mới (Chương III · Màn IV -> Chương VII · Màn VI) ===
  dict(id='c3-man4', arc='Chương III · Sumeru', src='c3_man4.txt', act='Chương III · Màn IV',
       title='Xích Thổ Chi Vương Và Tam Triều Thánh Giả', sub='Nhiệm vụ Ma Thần — Sumeru',
       hero='sc_c3_man4.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Cyno', role='Tổng Quản Mahamatra (tự trục xuất)', img='cyno_icon.png', desc='Cùng Lumine và Isak dò hỏi manh mối Người Giữ Làng tại Làng Aaru, lập kế hoạch xâm nhập doanh trại của Rahman.'),
         dict(name='Alhaitham', role='Quan Thư Ký Giáo Viện', img='alhaitham_icon.png', desc='Tự hành động điều tra ở sa mạc, phá giải cơ quan tại Bệnh viện Eleazar bỏ hoang và đọc chữ cổ trong lăng mộ.'),
         dict(name='Dehya', role='Lính đánh thuê Eremite · “Sư Tử Lửa”', img='dehya_icon.png', desc='Phối hợp giăng bẫy Hội Cấp Tiến ở Dịch Trạm Lữ Khách, đứng ra giao kèo bảo đảm trước Rahman để cứu nhóm Người Giữ Làng.'),
         dict(name='Candace', role='Hộ vệ Làng Aaru', img='candace_icon.png', desc='Thẩm vấn nhóm Hội Cấp Tiến, bảo vệ Làng Aaru và chăm sóc các Người Giữ Làng được giải cứu.'),
         dict(name='Isak', role='Cậu bé Làng Aaru', img='isak_icon.png', desc='Cùng Lumine và Cyno hỏi thăm dân làng và thâm nhập tìm lại ông nội của mình.'),
         dict(name='Rahman', role='Thủ lĩnh nhóm Eremite sa mạc', desc='Tín đồ Vua Deshret bắt cóc Người Giữ Làng vì hiểu lầm Thảo Thần; sau khi thấy di ngôn của tư tế Kasala, ông tỉnh ngộ và đồng ý hợp tác giải cứu Nahida.'),
         dict(name='Chú Anpu · Shani', role='Người dân Làng Aaru', desc='Trưởng làng Aaru và cô gái hai dòng máu tiết lộ manh mối về Bệnh viện Eleazar bỏ hoang.'),
         dict(name='Razak · Morghi · Judar', role='Học giả Giáo Viện', desc='Razak được cứu ở tầng hầm Bệnh viện Eleazar; Morghi và Judar phụ trách bắt giữ Người Giữ Làng.'),
         dict(name='Tư tế Kasala', role='Vị tư tế cuối cùng của Vua Deshret (ký ức)', desc='Hiện lên qua màn hình di ngôn cổ đại trong lăng mộ, kể lại sự hy sinh của Đại Vương Rukkhadevata để thanh tẩy tri thức cấm kỵ.'),
       ],
       pdf='', footer='Chương III · Màn IV — Xích Thổ Chi Vương Và Tam Triều Thánh Giả', side=False),
  dict(id='c3-man5', arc='Chương III · Sumeru', src='c3_man5.txt', act='Chương III · Màn V',
       title='Akasha Rung Động, Kiếp Hỏa Dâng Trào', sub='Nhiệm vụ Ma Thần — Sumeru',
       hero='sc_c3_man5.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Nahida', role='Tiểu Vương Kusanali · Thảo Thần', img='nahida_icon.png', desc='Sau khi được giải thoát khỏi Thánh Địa Surasthana, cô cùng Lumine vượt 168 vòng mộng cảnh đánh bại Shouki no Kami và thực hiện di nguyện thanh tẩy Cây Thế Giới.'),
         dict(name='Alhaitham', role='Quan Thư Ký Giáo Viện', img='alhaitham_icon.png', desc='Lên kế hoạch tráo Hũ Tri Thức giả đánh lừa Đại Hiền Giả Azar và tạm thời xử lý công vụ Giáo Viện hậu biến cố.'),
         dict(name='Cyno', role='Tổng Quản Mahamatra', img='cyno_icon.png', desc='Trực tiếp đột kích bắt giữ Azar tại Thánh Địa Surasthana và chính thức phục chức.'),
         dict(name='Dehya', role='“Sư Tử Lửa” · Eremite', img='dehya_icon.png', desc='Điều tra tung tích Dottore tại Cảng Ormos và dẫn đội Eremite giải cứu nhóm Lumine.'),
         dict(name='Tighnari', role='Đội Trưởng Kiểm Lâm Rừng Avidya', img='tighnari_icon.png', desc='Bảo vệ Haypasia tại Pardis Dhyai và chăm sóc Lumine phục hồi ở Làng Gandharva.'),
         dict(name='Collei', role='Kiểm lâm tập sự', img='collei_icon.png', desc='Bình phục hoàn toàn khỏi bệnh Eleazar sau khi Cây Thế Giới được thanh tẩy.'),
         dict(name='Nilou', role='Vũ công Nhà Hát Zubayr', img='nilou_icon.png', desc='Múa trước cổng Giáo Viện để kích hoạt lệnh cấm giả, mở màn kế hoạch giải cứu Thảo Thần và chủ trì tiệc mừng chiến thắng.'),
         dict(name='Dunyarzad', role='Tiểu thư nhà Homayani', img='dunyarzad_icon.png', desc='Khỏi hẳn bệnh Eleazar và tham dự lễ hội mừng chiến thắng tại Đại Khu Bazaar.'),
         dict(name='Candace', role='Hộ vệ Làng Aaru', img='candace_icon.png', desc='Hỗ trợ giữ hậu phương và hỏi thăm người dân Làng Aaru sau biến cố.'),
         dict(name='Rahman', role='Thủ lĩnh Eremite', desc='Phối hợp nhóm Eremite hành động theo kế hoạch của Alhaitham và tiếp tục ở lại hỗ trợ Làng Aaru.'),
         dict(name='Setaria', role='Cựu trợ lý Đại Hiền Giả', img='setaria_icon.png', desc='Sau biến cố, cô cùng Cyno và Rahman ở lại sa mạc hỗ trợ đời sống dân chúng.'),
         dict(name='Isak', role='Cậu bé Làng Aaru', img='isak_icon.png', desc='Cải trang làm Tiểu Vương Kusanali để đánh lạc hướng vệ binh Giáo Viện.'),
         dict(name='Azar', role='Đại Hiền Giả Giáo Viện', img='azar_icon.png', desc='Chủ mưu kế hoạch tạo thần nhân tạo và giam cầm Nahida; cuối cùng bị cách chức và đày về Rừng Avidya sám hối.'),
         dict(name='Dottore', role='Quan Chấp Hành Fatui thứ hai', img='dottore_icon.png', desc='Kẻ đứng sau thí nghiệm tạo thần; giao dịch hai viên Gnosis với Nahida bằng việc xóa bỏ các phân mảnh của chính mình và hé lộ bầu trời Teyvat là giả.'),
         dict(name='Scaramouche · Shouki no Kami', role='Quan Chấp Hành Fatui · “Vị Thần Bất Diệt”', img='shouki_icon.png', desc='Hóa thân thành “Vị Thần Bất Diệt Của Trí Tuệ Ẩn Mật” trong công xưởng ngầm, thất bại trước Lumine và mất Gnosis Lôi.'),
         dict(name='Đại Vương Rukkhadevata', role='Từ Thọ Vương Tiền Nhiệm (ý thức)', desc='Gửi lại di nguyện “Hãy để thế giới lãng quên ta hoàn toàn” giúp Nahida thanh tẩy tận gốc tri thức cấm kỵ khỏi Cây Thế Giới.'),
         dict(name='Kaveh', role='Kiến trúc sư Học Phái Kshahrewar', img='kaveh_icon.png', desc='Vừa trở về từ công trình sa mạc và khắc khẩu cùng Alhaitham tại Cung Điện Daena.'),
         dict(name='Vihar · Sheikh Zubayr · Haypasia', role='Đồng minh ở Đại Khu Bazaar & Pardis Dhyai', desc='Hỗ trợ thực hiện kế hoạch giải cứu và hồi phục sau sự kiện.'),
       ],
       pdf='', footer='Chương III · Màn V — Akasha Rung Động, Kiếp Hỏa Dâng Trào', side=False),
  dict(id='cd-man2-1', arc='Chương III · Sumeru', src='cd_man2_1.txt', act='Chương Đệm · Màn II.1',
       title='Cố Nhân Xa Lạ', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương Đệm · Màn III — Chương Phong Đỏ - Màn I (Kaedehara Kazuha)',
       hero='sc_cd_man2_1.jpg', thumb='sc_cd_man2_1.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Kaedehara Kazuha', role='Ronin Samurai · Truyền nhân Trường Phái Isshin', img='kazuha_icon.png', desc='Từ chối lời đề nghị phục chức gia chủ để đi cùng Lumine truy tìm kẻ tập kích, thu phục thanh yêu đao và rèn lại nó thành vũ khí đồng hành.'),
         dict(name='Kujou Kamaji', role='Đại diện nhà Kujou · Hiệp Hội Tenryou', desc='Đề xuất khôi phục danh dự và gia sản nhà Kaedehara cho Kazuha, đồng thời xử lý ổn thỏa vụ việc của Yuuya.'),
         dict(name='Amenoma Tougo', role='Thợ rèn chủ Xưởng Rèn Amenoma', desc='Cung cấp manh mối về cháu trai Yuuya mất tích và cho Kazuha mượn đe rèn lại thanh danh đao.'),
         dict(name='Amenoma Yuuya', role='Samurai nhà Amenoma', desc='Cháu trai của Amenoma Tougo bị thanh yêu đao chiếm giữ thân xác trước khi được Kazuha giải thoát.'),
         dict(name='Kagotsurube Isshin', role='Thanh yêu đao Trường Phái Isshin', desc='Thanh đao có ý thức mang tàn dư Họa Thần; sau khi thử thách Kazuha ở căn cứ nhà Takatsukasa, nó hối cải và xin được rèn lại.'),
         dict(name='Chao · Ryuuji · Nagato Sachiko · Murayama', role='Thuyền viên, thám tử và người dân Inazuma', desc='Những nhân chứng và người quen giúp lần theo tung tích vụ mất tích tại Thành Inazuma.'),
       ],
       pdf='', footer='Chương Đệm · Màn II.1 — Cố Nhân Xa Lạ', side=True),
  dict(id='cd-man3', arc='Chương III · Sumeru', src='cd_man3.txt', act='Chương Đệm · Màn III',
       title='Cội Nguồn Nghiêng Ngả', sub='Nhiệm vụ Ma Thần — Sumeru',
       hero='sc_cd_man3.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Nahida', role='Tiểu Vương Kusanali · Thảo Thần', img='nahida_icon.png', desc='Giám sát cựu Quan Chấp Hành thứ sáu và sao lưu ký ức của anh dưới dạng truyện cổ tích trước khi biến cố Cây Thế Giới xảy ra.'),
         dict(name='Scaramouche / Kẻ Lang Thang', role='Kẻ lữ hành · cựu Kabukimono', img='wanderer_icon.png', desc='Tự xóa tên mình khỏi Cây Thế Giới ở Tatarasuna; sau khi sống một quãng đời bình lặng, anh chủ động tiếp nhận lại ký ức cũ, nhận Vision Phong và mang tên mới “Kẻ Lang Thang”.'),
         dict(name='Dottore', role='Quan Chấp Hành Fatui (ký ức)', img='dottore_icon.png', desc='Xuất hiện trong ký ức tại Tatarasuna 400 năm trước dưới vỏ bọc kỹ sư Fontaine “Escher”, kẻ đã phản bội Niwa và đầu độc lò luyện.'),
         dict(name='Niwa · Katsuragi', role='Truyền nhân Tatarasuna (ký ức)', desc='Những người thân quen cũ của Kabukimono trong bi kịch Tatarasuna hiện lên qua dòng ký ức.'),
         dict(name='Amenoma Tougo', role='Thợ rèn chủ Xưởng Rèn Amenoma', desc='Cung cấp thông tin lịch sử về hệ phái Raiden Gokaden sau khi lịch sử bị sửa đổi.'),
         dict(name='Xavier · Hirotatsu · bà Furuta · Aqaba · Sawada', role='Kỹ sư, hầu cận Inazuma và học giả Sumeru', desc='Các nhân chứng giúp Lumine kiểm chứng sự thay đổi của lịch sử hậu biến cố Cây Thế Giới.'),
       ],
       pdf='', footer='Chương Đệm · Màn III — Cội Nguồn Nghiêng Ngả', side=False),
  dict(id='c3-man6', arc='Chương III · Sumeru', src='c3_man6.txt', act='Chương III · Màn VI',
       title='Caribert', sub='Nhiệm vụ Ma Thần — Sumeru',
       hero='nc_caribert.png',
       cast=[LUMINE, PAIMON,
         dict(name='Kaeya', role='Đội Trưởng Kỵ Binh · Đội Kỵ Sĩ Tây Phong', img='kaeya_icon.png', desc='Gặp Lumine ở Cảng Ormos và tiết lộ họ Alberich của mình thuộc gia tộc sáng lập Giáo Đoàn Vực Sâu.'),
         dict(name='Dainsleif', role="“Kiếm Sĩ Hoàng Hôn” của Khaenri'ah", img='dainsleif_icon.png', desc='Cùng Lumine tiến vào Rừng Avidya điều tra dấu tích Giáo Đoàn Vực Sâu và rời đi trước để tránh ảnh hưởng lên ký ức.'),
         dict(name='Chlothar Alberich', role="“Eide” · Quý tộc Khaenri'ah", desc='Người đàn ông bất tử xuất hiện trong ký ức của Aether, tìm thuốc giải cho con trai Caribert và lập nên Giáo Đoàn Vực Sâu.'),
         dict(name='Caribert', role='Cậu bé Hilichurl con của Eide', desc='Con trai của Chlothar và một phụ nữ Mondstadt; tỉnh lại ý thức trong khoảnh khắc gỡ bỏ mặt nạ.'),
         dict(name='Aether', role='Anh trai song sinh của Lumine (ký ức)', img='aether_icon.png', desc='Hiện ra qua mảnh gương vỡ và ký ức hàng trăm năm trước đồng hành cùng Chlothar Alberich.'),
         dict(name='Masrur · Eymen · Sứ Đồ Vận Mệnh', role='Cư dân Cảng Ormos và sinh mệnh Vực Sâu', desc='Người đưa thư, chủ quán cơm và Sứ Đồ canh giữ mật thất bức tượng treo xích.'),
       ],
       pdf='', footer='Chương III · Màn VI — Caribert', side=False),
  dict(id='c4-man1', arc='Chương IV · Fontaine', src='c4_man1.txt', act='Chương IV · Màn I',
       title='Khúc Dạo Đầu Của Sương Trắng Và Sóng Đen', sub='Nhiệm vụ Ma Thần — Fontaine',
       hero='sc_c4_man1.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Dehya', role='Lính đánh thuê “Sư Tử Lửa”', img='dehya_icon.png', desc='Tiễn chân Lumine và Paimon tại Dịch Trạm Lữ Khách trên đường sang Fontaine.'),
         dict(name='Lyney', role='Ảo thuật gia tài danh Fontaine', img='lyney_icon.png', desc='Tiếp đón Lumine tại Cảng Romaritime, bất ngờ bị cáo buộc sát hại và bắt cóc trong màn ảo thuật tại Viện Ca Kịch Epiclese.'),
         dict(name='Lynette', role='Em gái và trợ thủ của Lyney', img='lynette_icon.png', desc='Đồng hành cùng anh trai trong buổi diễn và hỗ trợ điều tra minh oan.'),
         dict(name='Freminet', role='Thợ lặn người Fontaine', img='freminet_icon.png', desc='Em trai trong gia đình của Lyney, gặp Lumine ở Đài Phun Nước Lucine và kể câu chuyện trời mưa của Long Vương.'),
         dict(name='Furina', role='Thủy Thần của Fontaine', img='furina_icon.png', desc='Đón chào Lumine ngay tại cảng với phong thái kịch tính và giữ vai trò nguyên cáo đối chất tại Viện Ca Kịch Epiclese.'),
         dict(name='Neuvillette', role='Thẩm Phán Tối Cao của Fontaine', img='neuvillette_icon.png', desc='Chủ tọa phiên tòa xét xử Lyney tại Viện Ca Kịch Epiclese.'),
         dict(name='Clorinde', role='Đấu Sĩ Đại Diện Fontaine', img='clorinde_icon.png', desc='Xuất hiện bên cạnh Thủy Thần Furina tại cảng đón đoàn.'),
         dict(name='Charlotte', role='Phóng viên Tòa Soạn Chim Hơi Nước', img='charlotte_icon.png', desc='Theo sát săn tin tại phiên tòa ở Viện Ca Kịch Epiclese.'),
         dict(name='Childe', role='Quan Chấp Hành Fatui', img='childe_icon.png', desc='Có mặt tại Fontaine, gửi nhờ Lumine giữ hộ Vision Thủy đang mất ổn định rồi rời đi.'),
         dict(name='Navia', role='Hội trưởng Spina di Rosula', img='navia_icon.png', desc='Phối hợp cùng Lumine thu thập chứng cứ, giải mã vụ hộp ảo thuật và chứng minh sự vô tội cho Lyney.'),
         dict(name='Melus và Silver', role='Cận vệ của Spina di Rosula', desc='Hai tùy tùng tận tụy luôn đi bên cạnh hỗ trợ Navia điều tra.'),
         dict(name='Cowell · Vaughn · Liliane · Tristane', role='Nhân chứng và đội điều tra Epiclese', desc='Trợ lý sân khấu, hiến binh liên quan đường dây Nước Biển Khởi Nguyên, nữ đạo chích Mondstadt và hiến binh Melusine gác cổng.'),
       ],
       pdf='', footer='Chương IV · Màn I — Khúc Dạo Đầu Của Sương Trắng Và Sóng Đen', side=False),
  dict(id='c4-man2', arc='Chương IV · Fontaine', src='c4_man2.txt', act='Chương IV · Màn II',
       title='Như Làn Mưa Nhẹ Không Rõ Nguyên Nhân', sub='Nhiệm vụ Ma Thần — Fontaine',
       hero='sc_c4_man2.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Navia', role='Hội trưởng Spina di Rosula', img='navia_icon.png', desc='Cùng Lumine lần theo vụ án “Thiếu Nữ Mất Tích Hàng Loạt” để minh oan cho cái chết của cha mình là cố hội trưởng Callas.'),
         dict(name='Melus và Silver', role='Tùy tùng trung thành của Navia', desc='Tiết lộ sự thật ba năm trước về việc Callas bảo vệ con gái và hỗ trợ khám xét chứng cứ.'),
         dict(name='Clorinde', role='Đấu Sĩ Đại Diện Fontaine', img='clorinde_icon.png', desc='Đứng ra giải cứu Navia khỏi đội Robot Hiến Binh tại cầu cảng và làm chứng trước tòa.'),
         dict(name='Neuvillette', role='Thẩm Phán Tối Cao của Fontaine', img='neuvillette_icon.png', desc='Chủ trì phiên xét xử Childe và Marcel (Vacher), trực tiếp đến viếng mộ Callas giữa cơn mưa.'),
         dict(name='Furina', role='Thủy Thần của Fontaine', img='furina_icon.png', desc='Tham dự phiên tòa và ngỡ ngàng trước phán quyết ngoài dự liệu của Cỗ Máy Chỉ Thị.'),
         dict(name='Childe', role='Quan Chấp Hành Fatui', img='childe_icon.png', desc='Bị Cỗ Máy Chỉ Thị Phán Quyết tuyên có tội một cách bí ẩn và bị áp giải vào Pháo Đài Meropide.'),
         dict(name='Marcel (Vacher)', role='Hội trưởng Thương Hội Cabriere', desc='Kẻ chủ mưu đường dây Sinthe và vụ bắt cóc các thiếu nữ suốt hai mươi năm, cuối cùng đối mặt linh hồn Vigneire ở Đài Phun Nước Lucine.'),
         dict(name='Sedene · Florent · Esmond', role='Nhân viên Palais Mermonia và Spina di Rosula', desc='Hỗ trợ truyền tin và áp giải phạm nhân tại Fontaine.'),
       ],
       pdf='', footer='Chương IV · Màn II — Như Làn Mưa Nhẹ Không Rõ Nguyên Nhân', side=False),
  dict(id='c4-man3', arc='Chương IV · Fontaine', src='c4_man3.txt', act='Chương IV · Màn III',
       title='Ngôi Sao Tỏa Sáng Dưới Biển Sâu', sub='Nhiệm vụ Ma Thần — Fontaine',
       hero='sc_c4_man3.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Neuvillette', role='Thẩm Phán Tối Cao Fontaine', img='neuvillette_icon.png', desc='Đề nghị Lumine nhận tội giả vào Pháo Đài Meropide để âm thầm điều tra vụ Childe mất tích.'),
         dict(name='Furina', role='Thủy Thần của Fontaine', img='furina_icon.png', desc='Tiếp đón Quan Chấp Hành Arlecchino trong buổi tiệc trà ngoại giao cùng Neuvillette.'),
         dict(name='Arlecchino', role='Quan Chấp Hành thứ tư của Fatui', img='arlecchino_icon.png', desc='Đến Palais Mermonia yêu cầu được điều tra tung tích của Childe và đồng ý phương án của Neuvillette.'),
         dict(name='Charlotte', role='Phóng viên Chim Hơi Nước', img='charlotte_icon.png', desc='Gặp Lumine ở Tiệm Cà Phê Lutece và nhờ tìm hiểu về Công Tước Wriothesley.'),
         dict(name='Wriothesley', role='Công Tước · Người quản lý Pháo Đài Meropide', img='wriothesley_icon.png', desc='Trực tiếp tiếp đón tù nhân mới và dẫn Lumine đi tham quan Pháo Đài Meropide.'),
         dict(name='Sigewinne', role='Y tá trưởng Phòng Y Tế Pháo Đài Meropide', img='sigewinne_icon.png', desc='Cô y tá Melusine tiếp đón Lumine và chăm sóc trật tự khu y tế ngục giam.'),
         dict(name='Lyney', role='Ảo thuật gia · tù nhân điều tra', img='lyney_icon.png', desc='Cố ý gây án nhỏ để vào Pháo Đài Meropide cùng hai em truy tìm bí mật khu vực cấm.'),
         dict(name='Lynette', role='Thành viên Căn Nhà Hơi Ấm', img='lynette_icon.png', desc='Phối hợp cùng Lyney thực hiện màn dàn cảnh vào tù điều tra.'),
         dict(name='Childe', role='Quan Chấp Hành Fatui (mộng cảnh)', img='childe_icon.png', desc='Xuất hiện qua những mảnh thị kiến trong giấc ngủ của Lumine trước lúc vượt ngục.'),
         dict(name='Deakin · Vidoc · Fielding · Leonide · Marette', role='Cai ngục và tù nhân Pháo Đài Meropide', desc='Hướng dẫn sinh hoạt bằng Phiếu Đặc Cách và tiết lộ manh mối những “quy tắc ngầm”.'),
       ],
       pdf='', footer='Chương IV · Màn III — Ngôi Sao Tỏa Sáng Dưới Biển Sâu', side=False),
  dict(id='c4-man4', arc='Chương IV · Fontaine', src='c4_man4.txt', act='Chương IV · Màn IV',
       title='Thảm Họa Cận Kề', sub='Nhiệm vụ Ma Thần — Fontaine',
       hero='sc_c4_man4.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Lyney', role='Ảo thuật gia Căn Nhà Hơi Ấm', img='lyney_icon.png', desc='Đối mặt Wriothesley khi em gái mất tích và cùng cả nhóm tìm cách ứng phó thảm họa.'),
         dict(name='Lynette', role='Thành viên Căn Nhà Hơi Ấm', img='lynette_icon.png', desc='Giả bệnh vào Phòng Y Tế điều tra và bị Wriothesley giữ lại làm con tin đàm phán.'),
         dict(name='Freminet', role='Thợ lặn Căn Nhà Hơi Ấm', img='freminet_icon.png', desc='Lặn xuống đường ống ngập nước truy tìm dấu vết Childe và suýt gặp nạn bởi Nước Biển Khởi Nguyên.'),
         dict(name='Wriothesley', role='Công Tước Pháo Đài Meropide', img='wriothesley_icon.png', desc='Hé lộ bí mật cánh cửa cống chặn Nước Biển Khởi Nguyên và dự án con thuyền lớn đóng ngầm dưới pháo đài.'),
         dict(name='Sigewinne', role='Y tá trưởng Pháo Đài Meropide', img='sigewinne_icon.png', desc='Hỗ trợ Công Tước bảo vệ an toàn cho anh em nhà Lyney và tù nhân khi cửa cống rò rỉ.'),
         dict(name='Clorinde', role='Đấu Sĩ Đại Diện Fontaine', img='clorinde_icon.png', desc='Nhận ủy thác của Wriothesley, kịp thời lặn xuống cứu Freminet và cùng Công Tước chốt chặn khu vực cấm.'),
         dict(name='Neuvillette', role='Thẩm Phán Tối Cao · Thủy Long Vương', img='neuvillette_icon.png', desc='Trực tiếp lao xuống Khu Vực Cấm đẩy lùi Nước Biển Khởi Nguyên và lần đầu thừa nhận thân phận Thủy Long Vương.'),
         dict(name='Furina', role='Thủy Thần Fontaine', img='furina_icon.png', desc='Dự tiệc trà cùng Arlecchino dưới sự bảo vệ ngầm của Lumine và Paimon.'),
         dict(name='Arlecchino', role='Quan Chấp Hành Fatui “Người Hầu”', img='arlecchino_icon.png', desc='Chất vấn Furina về lời tiên tri diệt vong và kể lại lần chạm mặt khiến cô nghi ngờ Furina không giữ Gnosis.'),
         dict(name='Childe', role='Quan Chấp Hành Fatui (cắt cảnh)', img='childe_icon.png', desc='Xuất hiện giữa lòng Biển Khởi Nguyên đối diện bóng dáng khổng lồ của dị thú ngoài tinh cầu.'),
         dict(name='Cuistot · Laverune · Jurieu · Lourvine', role='Cư dân và kỹ sư Pháo Đài Meropide', desc='Hỗ trợ tin tức và vận hành công trình tàu ngầm.'),
       ],
       pdf='', footer='Chương IV · Màn IV — Thảm Họa Cận Kề', side=False),
  dict(id='c4-man5', arc='Chương IV · Fontaine', src='c4_man5.txt', act='Chương IV · Màn V',
       title='Vũ Điệu Của Tội Lỗi', sub='Nhiệm vụ Ma Thần — Fontaine',
       hero='nc_fontaine_completeness.png',
       cast=[LUMINE, PAIMON,
         dict(name='Navia', role='Hội trưởng Spina di Rosula', img='navia_icon.png', desc='Cùng Lumine khám phá phiến đá tiên tri tại di tích Poisson và giữ vai trò trợ lý công tố trước tòa.'),
         dict(name='Neuvillette', role='Thủy Long Vương · Thẩm Phán Tối Cao', img='neuvillette_icon.png', desc='Tiếp nhận toàn bộ Quyền Năng Thủy Long sau cái chết của Focalors, xá tội cho người dân Fontaine và dẹp yên đại hồng thủy.'),
         dict(name='Furina', role='“Thủy Thần” suốt 500 năm', img='furina_icon.png', desc='Giữ vững lời hẹn ước cô độc suốt năm trăm năm trên sân khấu nhân thế trước khi được giải thoát khỏi vai diễn.'),
         dict(name='Focalors', role='Ma Thần Thủy · Thần Công Lý', desc='Bản thể thần tính ẩn trong Cỗ Máy Chỉ Thị; tự hiến tế chính mình và ngai Thủy Thần để cứu toàn dân Fontaine khỏi lời tiên tri.'),
         dict(name='Wriothesley', role='Công Tước Pháo Đài Meropide', img='wriothesley_icon.png', desc='Khởi hành con tàu Wingalet cứu vớt toàn bộ cư dân Fontaine trong trận đại hồng thủy.'),
         dict(name='Sigewinne', role='Y tá trưởng Pháo Đài Meropide', img='sigewinne_icon.png', desc='Hỗ trợ kiểm chứng phản ứng của Furina trước Nước Biển Khởi Nguyên pha loãng.'),
         dict(name='Arlecchino', role='Quan Chấp Hành Fatui “Người Hầu”', img='arlecchino_icon.png', desc='Chi viện vật tư cho Thị Trấn Poisson và tiếp nhận Gnosis Thủy từ Neuvillette sau thảm họa.'),
         dict(name='Lyney', role='Ảo thuật gia Căn Nhà Hơi Ấm', img='lyney_icon.png', desc='Chế tạo cái bẫy hộp ảo thuật đưa Furina lên vành móng ngựa và tham gia cứu nạn Poisson.'),
         dict(name='Lynette · Freminet', role='Thành viên Căn Nhà Hơi Ấm', img='lynette_icon.png', desc='Tìm lại phiến đá tiên tri đầu tiên bị thất lạc và góp sức cứu hộ trong đại hồng thủy.'),
         dict(name='Clorinde', role='Đấu Sĩ Đại Diện', img='clorinde_icon.png', desc='Sẵn sàng nghênh chiến trên sân khấu ép Furina đối diện phiên xét xử.'),
         dict(name='Mona', role='Nhà chiêm tinh học từ Mondstadt', img='mona_icon.png', desc='Kết nối liên lạc tới sư phụ Barbeloth và Ma Nữ “N” Nicole để giải mã lỗ hổng lời tiên tri.'),
         dict(name='Nicole', role='Ma Nữ “N” · Hội Ma Nữ (âm thanh)', img='nicole_icon.png', desc='Truyền âm gợi ý cho Lumine tại Fleuve Cendre về bản chất không thể thay đổi trên bề mặt của lời tiên tri.'),
         dict(name='Charlotte', role='Phóng viên Chim Hơi Nước', img='charlotte_icon.png', desc='Ghi lại những hình ảnh và chứng từ lịch sử của đại hồng thủy Fontaine.'),
         dict(name='Skirk', role='Sư phụ của Childe', img='skirk_icon.png', desc='Xuất hiện thu hồi Thôn Tinh Kình Ngư và tiết lộ bản chất Gnosis là di vật của Kẻ Đổ Bộ Thứ Ba.'),
         dict(name='Thôn Tinh Kình Ngư', role='Dị thú ngoài tinh cầu', img='narwhal_icon.png', desc='Đột nhập Viện Ca Kịch Epiclese và bị Lumine cùng Neuvillette hợp lực đánh bại.'),
         dict(name='Childe', role='Quan Chấp Hành Fatui (cắt cảnh)', img='childe_icon.png', desc='Kiệt sức sau trận chiến kéo dài chống Thôn Tinh Kình Ngư trước khi được Skirk đưa đi.'),
         dict(name='Melus và Silver', role='Tùy tùng đã khuất của Navia', desc='Xuất hiện bảo vệ Navia dưới hình dạng Tinh Linh Nước Trong giữa dòng Nước Biển Khởi Nguyên.'),
       ],
       pdf='', footer='Chương IV · Màn V — Vũ Điệu Của Tội Lỗi', side=False),
  dict(id='c4-man6', arc='Chương IV · Fontaine', src='c4_man6.txt', act='Chương IV · Màn VI',
       title='Câu Chuyện Trước Khi Ngủ', sub='Nhiệm vụ Ma Thần — Sumeru',
       hero='sc_c4_man6.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Katheryne', role='Hiệp Hội Nhà Mạo Hiểm Thành Sumeru', img='katheryne_icon.png', desc='Giao ủy thác điều tra người mất tích bí ẩn tại Làng Vimara.'),
         dict(name='Dainsleif', role='“Kiếm Sĩ Hoàng Hôn”', img='dainsleif_icon.png', desc='Đồng hành cùng Lumine truy tìm mắt máy cày và đối đầu trực diện Giáo Đoàn Vực Sâu cùng Hoàng Tử.'),
         dict(name='Caribert', role='Ý thức còn sót lại trong “Máy Dệt Vận Mệnh”', desc='Hoàn thiện Máy Dệt Vận Mệnh bằng việc cấy ký ức giả tại Làng Vimara và mở không gian trò chuyện cho hai anh em song sinh.'),
         dict(name='Aether', role='Anh trai song sinh của Lumine · Hoàng Tử Vực Sâu', img='aether_icon.png', desc='Đánh bại Dainsleif và có cuộc trò chuyện bình lặng hiếm hoi cùng em gái trong không gian ý thức trước khi Máy Dệt tan biến.'),
         dict(name='Atossa · Bahram · Amadhiah', role='Cư dân và trưởng làng Vimara', desc='Những người vô tình mang ký ức giả về Caribert trước khi phần ký ức ấy mờ phai.'),
       ],
       pdf='', footer='Chương IV · Màn VI — Câu Chuyện Trước Khi Ngủ', side=False),
  dict(id='c5-man1', arc='Chương V · Natlan', src='c5_man1.txt', act='Chương V · Màn I',
       title='Sắc Hoa Rực Rỡ Trong Hành Trình Nắng Cháy', sub='Nhiệm vụ Ma Thần — Natlan',
       hero='sc_c5_man1.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Charlotte · Navia · Clorinde · Furina', role='Những người bạn Fontaine', img='furina_icon.png', desc='Tiễn chân Lumine và Paimon tại Cảng Romaritime trước khi khởi hành sang Natlan.'),
         dict(name='Kachina', role='Chiến binh Con Của Tiếng Vang · Tên Cổ Uthabiti', img='kachina_icon.png', desc='Cô bé kiên cường vượt qua tự ti, bắt cặp cùng Mualani chiến thắng vòng loại và bước vào Trận Chiến Người Gác Đêm.'),
         dict(name='Mualani', role='Chiến binh Cư Dân Suối Nước', img='mualani_icon.png', desc='Bạn thân của Kachina, đón chào Lumine bước vào Natlan và đưa mọi người về thăm quê nhà.'),
         dict(name='Kinich', role='Thợ săn Dòng Dõi Vườn Treo', img='kinich_icon.png', desc='Chiến binh lý trí tham dự Nghi Lễ Hành Hương Về Lửa Thánh cùng cộng sự Ajaw.'),
         dict(name='Ajaw', role="“Thánh Long K'uhul Ajaw Toàn Năng”", desc='Sinh vật hai chiều ồn ào đồng hành bên Kinich.'),
         dict(name='Mavuika', role='Hỏa Thần đương nhiệm của Natlan', img='mavuika_icon.png', desc='Chủ trì Nghi Lễ Hành Hương Về Lửa Thánh tại Đấu Trường.'),
         dict(name='Nhóc Con', role='Chú Tepetlisaur nhỏ', desc='Bạn đồng hành Saurian đi theo Lumine và Paimon khắp Đấu Trường Lửa Thánh.'),
         dict(name='Atea · Amina', role='Chiến binh kỳ cựu và thủ lĩnh Cư Dân Suối Nước', desc='Atea giữ nụ cười kiên cường dù mang vết thương Vực Sâu nặng từ năm xưa; Amina dẫn dắt bộ tộc.'),
         dict(name='Pacal · Cival · Lisa · Venti', role='Tộc trưởng Con Của Tiếng Vang & hồi ức Mondstadt', desc='Những nhân vật hỗ trợ tại đấu trường và hiện lên trong hồi tưởng về khả năng thanh tẩy Vực Sâu của Lumine.'),
       ],
       pdf='', footer='Chương V · Màn I — Sắc Hoa Rực Rỡ Trong Hành Trình Nắng Cháy', side=False),
  dict(id='c5-man2', arc='Chương V · Natlan', src='c5_man2.txt', act='Chương V · Màn II',
       title='Đá Đen Ẩn Dưới Lớp Đá Trắng', sub='Nhiệm vụ Ma Thần — Natlan',
       hero='sc_c5_man2.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Mualani', role='Chiến binh Cư Dân Suối Nước · Tên Cổ Umoja', img='mualani_icon.png', desc='Thức tỉnh danh hiệu anh hùng “Đoàn Kết” của Tupac, dẫn đầu chiến dịch xuống Vương Quốc Dạ Thần cứu Kachina.'),
         dict(name='Kachina', role='Chiến binh Con Của Tiếng Vang', img='kachina_icon.png', desc='Bị mắc kẹt trong Vương Quốc Dạ Thần vì Thơ Hoàn Hồn bất thường, được đồng đội và Lumine giải cứu trở về.'),
         dict(name='Mavuika', role='Hỏa Thần của Natlan', img='mavuika_icon.png', desc='Giao đấu rực lửa với Capitano, sẵn sàng thiêu rụi toàn bộ kỷ vật cá nhân suốt năm trăm năm để mở đường cứu đồng đội khỏi Dạ Thần.'),
         dict(name='Kinich', role='Chiến binh Dòng Dõi Vườn Treo · Tên Cổ Malipo', img='kinich_icon.png', desc='Một trong bốn anh hùng được Wayob công nhận, sát cánh giải cứu Kachina.'),
         dict(name='Chasca', role='Chiến binh Hội Hoa Vũ', img='chasca_icon.png', desc='Tham gia chiến dịch giải cứu Kachina để chuộc lại trách nhiệm của bản thân.'),
         dict(name='Iansan', role='Huấn luyện viên Cộng Đồng Trù Phú', img='iansan_icon.png', desc='Anh hùng đã thức tỉnh Tên Cổ, phối hợp cùng mọi người chống lại nguy cơ từ Vực Sâu.'),
         dict(name='Capitano', role='Quan Chấp Hành thứ nhất của Fatui', desc='Đích thân đối đầu Hỏa Thần Mavuika tại Đấu Trường Lửa Thánh trước khi được màn sương bí ẩn giải vây.'),
         dict(name='Chuychu', role='Bác sĩ hậu cần · em gái của Chasca', desc='Kiểm tra và thanh lọc ô nhiễm Vực Sâu cho cả nhóm sau khi thoát khỏi Vương Quốc Dạ Thần.'),
         dict(name='Vichama · Mallko · Wayna · Tupac · Hine · Atea', role='Chiến binh Dòng Dõi Vườn Treo, linh hồn anh hùng và kỷ vật quá khứ', desc='Những người thân và linh hồn đã khuất soi đường cho cả nhóm vượt qua cõi âm Vương Quốc Dạ Thần.'),
       ],
       pdf='', footer='Chương V · Màn II — Đá Đen Ẩn Dưới Lớp Đá Trắng', side=False),
  dict(id='c5-man3', arc='Chương V · Natlan', src='c5_man3.txt', act='Chương V · Màn III',
       title='Bên Kia Của Gương Và Khói', sub='Nhiệm vụ Ma Thần — Natlan',
       hero='sc_c5_man3.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Citlali', role='Đại Shaman “Bà Itztli” · Chủ Nhân Gió Đêm', img='citlali_icon.png', desc='Pháp sư tinh thông cổ sử và thuật Dạ Thần, phát hiện học trò Ororon đang bí mật cấu kết cùng Fatui.'),
         dict(name='Ororon', role='Thanh niên bộ tộc Chủ Nhân Gió Đêm', img='ororon_icon.png', desc='Chàng trai hiền lành mang linh hồn khiếm khuyết, chấp nhận hợp tác với Capitano nhằm tìm phương án tái thiết Địa Mạch cứu Natlan.'),
         dict(name='Xilonen', role='Thợ rèn Tên Cổ · Con Của Tiếng Vang', img='xilonen_icon.png', desc='Thợ thủ công thiên tài và một trong sáu anh hùng, nhận lời tìm cách chế tác Tên Cổ cho Lumine.'),
         dict(name='Capitano', role='Quan Chấp Hành thứ nhất của Fatui', desc='Chỉ huy lực lượng Fatui điều tra Thiết Bị Nguồn dưới lòng đất nhằm bảo toàn tương lai Natlan.'),
         dict(name='Mavuika', role='Hỏa Thần của Natlan', img='mavuika_icon.png', desc='Giữ vững kế hoạch sáu anh hùng bất chấp áp lực từ phương án thay thế của Capitano.'),
         dict(name='Chasca · Chuychu', role='Hai chị em Hội Hoa Vũ', img='chasca_icon.png', desc='Bám theo lực lượng Fatui tới khu khai quật Thiết Bị Nguồn.'),
         dict(name='Kinich · Mualani · Kachina · Iansan · Katheryne', role='Các đồng đội bộ tộc và Hiệp Hội Nhà Mạo Hiểm', img='katheryne_icon.png', desc='Phối hợp giữ phòng tuyến và chuyển giao tin tức giữa các bộ tộc trước sóng gió Vực Sâu.'),
       ],
       pdf='', footer='Chương V · Màn III — Bên Kia Của Gương Và Khói', side=False),
  dict(id='c5-man4', arc='Chương V · Natlan', src='c5_man4.txt', act='Chương V · Màn IV',
       title='Cầu Vồng Định Sẵn Sẽ Cháy', sub='Nhiệm vụ Ma Thần — Natlan',
       hero='sc_c5_man4.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Mavuika', role='Hỏa Thần của Natlan', img='mavuika_icon.png', desc='Tổng chỉ huy cuộc chiến bảo vệ toàn cõi Natlan và giải phóng sức mạnh Ngai Thần đánh bật cuộc xâm lăng Vực Sâu.'),
         dict(name='Capitano', role='Quan Chấp Hành Fatui', desc='Tạm đình chiến và đưa đại quân Fatui sát cánh bảo vệ dân thường Natlan chống lại Gosoythoth.'),
         dict(name='Citlali', role='Shaman Chủ Nhân Gió Đêm', img='citlali_icon.png', desc='Phát hiện cái giá sinh mạng mà Mavuika phải trả khi dùng quyền năng Ngai Thần và chuẩn bị rèn Tên Cổ cho Lumine.'),
         dict(name='Xilonen', role='Thợ rèn Tên Cổ · Tên Cổ Baraka', img='xilonen_icon.png', desc='Xin Dạ Thần vật dẫn ghi chiến tích để rèn Tên Cổ cho Lumine bất chấp tuổi thọ bản thân bị tiêu hao.'),
         dict(name='Ororon', role='Anh hùng thứ năm · Tên Cổ Bidii', img='ororon_icon.png', desc='Vượt qua tâm ma trong Di Tích Nguồn và được Sanhaj truyền thừa trở thành anh hùng thứ năm.'),
         dict(name='Chasca', role='Anh hùng thứ sáu · Tên Cổ Vuka', img='chasca_icon.png', desc='Vượt qua bi kịch mất đi em gái Chuychu để khống chế năng lượng Vực Sâu, trở thành anh hùng cuối cùng thức tỉnh.'),
         dict(name='Chuychu', role='Bác sĩ hậu cần · em gái của Chasca', desc='Hy sinh anh dũng trên chiến trường sơ tán ở Hội Hoa Vũ sau khi bị Vực Sâu ăn mòn nặng.'),
         dict(name='Kachina · Mualani · Kinich · Ajaw · Iansan', role='Các anh hùng và bạn đồng hành sáu bộ tộc', img='mualani_icon.png', desc='Hợp lực giữ vững chiến tuyến tại sáu bộ tộc và hội tụ quanh Lửa Thánh cùng Mavuika.'),
         dict(name='Yohualtecuhtin', role='Dạ Thần · Người cai quản Vương Quốc Dạ Thần', desc='Thiên Sứ cổ đại trao vật dẫn Địa Mạch và xác nhận truyền thừa anh hùng.'),
         dict(name='Sáu vị anh hùng xưa · Ronova · Gosoythoth', role='Quá khứ 500 năm trước & thế lực Vực Sâu', img='gosoythoth_icon.png', desc='Gồm Xbalanque và Chấp Chính Của Cái Chết trong ký ức cổ đại cùng Chúa Tể Hủy Diệt Gosoythoth.'),
       ],
       pdf='', footer='Chương V · Màn IV — Cầu Vồng Định Sẵn Sẽ Cháy', side=False),
  dict(id='c5-phandem', arc='Chương V · Natlan', src='c5_phandem.txt', act='Chương V · Phần Đệm',
       title='Vạn Hỏa Quy Nhất', sub='Nhiệm vụ Ma Thần — Natlan',
       hero='sc_c5_phandem.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Iansan', role='Huấn luyện viên Cộng Đồng Trù Phú · Tên Cổ Uwezo', img='iansan_icon.png', desc='Dẫn học viên từ Cộng Đồng Trù Phú sang giúp Hội Hoa Vũ tái thiết và hỗ trợ các chiến binh vượt qua sang chấn tinh thần.'),
         dict(name='Capitano', role='Quan Chấp Hành thứ nhất Fatui', desc='Mang Thuốc Thông Suốt tới cứu giúp Ocotlan và tiết lộ lời nguyền bất tử khắc nghiệt dưới lớp mặt nạ.'),
         dict(name='Mutota · Atoco · Cochitta · Cuallee · Ocotlan', role='Thủ lĩnh và chiến binh Hội Hoa Vũ', desc='Những người dân chịu tổn thất tâm lý nặng nề sau đại chiến Vực Sâu được Iansan và Lumine giúp đỡ.'),
         dict(name='Xilonen · Citlali · Ororon · Kinich · Ajaw · Mualani · Kachina · Chasca', role='Các đồng đội tập hợp tại Lò Rèn', img='xilonen_icon.png', desc='Cùng kể lại chiến tích của Lumine vào Sử Ký Hành Hương trước giờ rèn Tên Cổ.'),
       ],
       pdf='', footer='Chương V · Phần Đệm — Vạn Hỏa Quy Nhất', side=False),
  dict(id='c5-man5', arc='Chương V · Natlan', src='c5_man5.txt', act='Chương V · Màn V',
       title='Bài Thơ Về Sự Tái Sinh Rực Rỡ', sub='Nhiệm vụ Ma Thần — Natlan',
       hero='nc_natlan_endpoint.png',
       cast=[LUMINE, PAIMON,
         dict(name='Mavuika', role='Hỏa Thần Haborym của Natlan', img='mavuika_icon.png', desc='Sát cánh cùng Lumine tiến sâu vào Vương Quốc Dạ Thần tiêu diệt Chúa Tể Lửa Nguồn Ăn Mòn và khai mở kỷ nguyên mới.'),
         dict(name='Capitano', role='“Kỵ Sĩ Thiên Trụ” Thrain · Quan Chấp Hành thứ nhất', desc='Dùng nghịch lý bất tử để gánh thay cái giá sinh mạng cho Mavuika trước mặt Ronova, hợp nhất với Dạ Thần trên Ngai Lửa Nguồn.'),
         dict(name='Citlali · Xilonen', role='Đại Shaman và Thợ rèn Tên Cổ', img='citlali_icon.png', desc='Hoàn thành Tên Cổ *Tumaini (Hy Vọng)* cho Lumine và kiểm tra dòng Địa Mạch trước trận quyết chiến.'),
         dict(name='Kachina · Mualani · Kinich · Ajaw · Chasca · Iansan · Ororon', role='Sáu anh hùng và đồng đội sáu bộ tộc', img='chasca_icon.png', desc='Cùng sáu tộc trưởng tiễn đưa và tiếp sức cổ vũ cho Lumine và Mavuika xuyên suốt cuộc chiến.'),
         dict(name='Yohualtecuhtin', role='Dạ Thần · Chủ Nhân Vương Quốc Dạ Thần', desc='Đánh thức Nguyên Tố Hỏa cho Lumine và hợp nhất cùng Capitano để duy trì vĩnh viễn Địa Mạch Natlan.'),
         dict(name='Ronova', role='Chấp Chính Của Cái Chết · Cái Bóng của Thiên Lý', desc='Hiện thân trên bầu trời Ochkanatlan đòi cái giá tử vong trước khi buộc phải bảo toàn lời nguyền bất tử cho Thrain.'),
         dict(name='Gosoythoth', role='Chúa Tể Lửa Nguồn Ăn Mòn', img='gosoythoth_icon.png', desc='Sử dụng giọng nói của các Hỏa Thần tiền nhiệm công kích tinh thần trước khi bị Lumine và Mavuika thanh tẩy hoàn toàn.'),
         dict(name='Nhóc Con · Ayo · Hine · Atea · Vichama · Mallko · Chuychu · Guthred', role='Các linh hồn, cố nhân và Saurian đồng hành', desc='Hội tụ cổ vũ và hộ tống hai chiến binh đi qua vùng đất bóng tối tới thắng lợi cuối cùng.'),
       ],
       pdf='', footer='Chương V · Màn V — Bài Thơ Về Sự Tái Sinh Rực Rỡ', side=False),
  dict(id='cd-man3-1', arc='Chương V · Natlan', src='cd_man3_1.txt', act='Chương Đệm · Màn III.1',
       title='Báo Cáo Quan Sát Nhà Lữ Hành', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương Đệm · Màn IV — Chương Bạch Phấn chi Tử - Màn I (Albedo)',
       hero='nc_dragonspine.png', thumb='nc_dragonspine.png',
       cast=[LUMINE, PAIMON,
         dict(name='Albedo', role='Giả Kim Thuật Sĩ · Đội Trưởng Đội Điều Tra', img='albedo_icon.png', desc='Thực hiện chuỗi thực nghiệm nguyên tố, thế giới và sinh mệnh trên Long Tích Tuyết Sơn để tìm lời giải đánh thức hạt giống dị giới.'),
         dict(name='Sucrose', role='Phụ tá giả kim Đội Kỵ Sĩ Tây Phong', img='sucrose_icon.png', desc='Giới thiệu Lumine lên Long Tích Tuyết Sơn gặp sư phụ Albedo.'),
         dict(name='Rosaria', role='Nữ tu Giáo Hội Tây Phong', img='rosaria_icon.png', desc='Bám theo dấu vết lên núi tuyết theo dõi cuộc thực nghiệm và dặn Lumine đề phòng Albedo.'),
         dict(name='Barbara', role='Mục sư tế lễ Giáo Hội Tây Phong', img='barbara_icon.png', desc='Tìm gặp Rosaria ở chân núi tuyết để nhắc lịch tập hợp xướng.'),
         dict(name='Timaeus', role='Phụ tá giả kim', desc='Lên doanh trại núi tuyết tổng hợp số liệu giúp Albedo.'),
       ],
       pdf='', footer='Chương Đệm · Màn III.1 — Báo Cáo Quan Sát Nhà Lữ Hành', side=True),
  dict(id='cd-man4', arc='Chương V · Natlan', src='cd_man4.txt', act='Chương Đệm · Màn IV',
       title='Ngộ Biện', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='durin_splash.png',
       cast=[LUMINE, PAIMON,
         dict(name='Albedo', role='“Kreideprinz” · Giả Kim Thuật Sĩ', img='albedo_icon.png', desc='Dàn dựng hai phiên xét xử để dụ kẻ mạo danh từ xác ma long Durin lộ diện và chuyển hóa Durin Nhỏ thành con người.'),
         dict(name='Venti', role='Nhà thơ · Phong Thần Barbatos', img='venti_icon.png', desc='Trao Bộ Liên Lạc Dodoco, dệt mạng lưới gió bảo vệ thành và triệu tập Hội Nghị Ba Bên của Hội Ma Nữ.'),
         dict(name='Dahlia', role='Phó tế Giáo Hội Tây Phong', img='dahlia_icon.png', desc='Giữ vai trò bồi thẩm đoàn trong phiên tòa và điều phối tin tức giúp Phong Thần.'),
         dict(name='Jean · Kaeya · Diluc', role='Quyền Đội Trưởng, Đội Trưởng Kỵ Binh & Chủ Tửu Trang Dawn', img='jean_icon.png', desc='Jean chủ tọa phiên tòa và tổng chỉ huy phòng thủ thành; Kaeya bào chữa và sát cánh cùng Diluc trấn giữ cổng thành.'),
         dict(name='Durin', role='Chú rồng nhỏ từ Simulanka · nhân loại mới', img='durin_icon.png', desc='Lựa chọn bước sang kiếp sống mới mang trái tim thuần khiết qua phép giả kim của Albedo.'),
         dict(name='Eula · Sucrose · Rosaria · Barbara · Mona', role='Các Kỵ Sĩ, nữ tu và nhà chiêm tinh Mondstadt', img='mona_icon.png', desc='Điều chế thuốc, chữa thương, bói nước theo dõi toàn cục và giữ vững các cửa ải bảo vệ thành.'),
         dict(name='Amber · Mika · Klee · Bennett · Diona · Hertha', role='Thành viên Đội Kỵ Sĩ và cư dân Mondstadt', img='klee_icon.png', desc='Bảo vệ người dân tại nơi trú ẩn và vạch trần kẻ giả mạo từ tàn dư Durin.'),
         dict(name='Varka', role='Đại Đội Trưởng Đội Kỵ Sĩ Tây Phong (âm thanh)', img='varka_icon.png', desc='Vô tình bắt máy Bộ Liên Lạc Dodoco từ vùng cực bắc giữa lúc đang giao chiến.'),
         dict(name='Alice · Barbeloth', role='Hai Ma Nữ Hội Ma Nữ (Dodoco)', desc='Xuất hiện dưới hình dạng Dodoco chủ trì cuộc họp và thí luyện Ván Cờ Trước Ngưỡng Cửa.'),
       ],
       pdf='', footer='Chương Đệm · Màn IV — Ngộ Biện', side=False),
  dict(id='c5-man6', arc='Chương V · Natlan', src='c5_man6.txt', act='Chương V · Màn VI',
       title='Thời Không Mà Ta Tồn Tại', sub='Nhiệm vụ Ma Thần — Natlan',
       hero='sc_c5_man6.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Iansan', role='Huấn luyện viên Cộng Đồng Trù Phú', img='iansan_icon.png', desc='Phát hiện cuộc tập kích bất ngờ của Giáo Đoàn Vực Sâu và cùng Lumine giữ vững phòng tuyến bộ tộc.'),
         dict(name='Mavuika', role='Hỏa Thần Natlan', img='mavuika_icon.png', desc='Điều phối lực lượng phòng thủ từ Đấu Trường Lửa Thánh trước đợt tấn công mới.'),
         dict(name='Citlali', role='Shaman Chủ Nhân Gió Đêm', img='citlali_icon.png', desc='Cảm nhận tạp âm bất thường trong Địa Mạch Natlan và trực tiếp ra trận đẩy lùi Vực Sâu.'),
         dict(name='Direidyth', role="Thiếu nữ Khaenri'ah năm trăm năm trước", desc='Bước qua giao điểm thời không gặp Lumine tại Natlan, trao chiếc chìa khóa phi thuyền định mệnh trước lúc lịch sử khép lại.'),
         dict(name='Dainsleif', role='“Kiếm Sĩ Hoàng Hôn”', img='dainsleif_icon.png', desc='Đột phá phòng tuyến Giáo Đoàn Vực Sâu và đối mặt chính người thầy cũ Haden tại Thành Tro Tàn.'),
         dict(name='Haden', role='Kẻ Rửa Tội Vực Sâu', img='abyss_baptist_icon.png', desc="Sư phụ Kiếm Thuật Hắc Xà của Dainsleif từ Khaenri'ah năm xưa nay trấn giữ tổng bộ Giáo Đoàn Vực Sâu."),
         dict(name='Aether', role='Anh trai song sinh của Lumine · Hoàng Tử Vực Sâu', img='aether_icon.png', desc="Xuất hiện bên cạnh Bản Đồ Của Thế Giới Mới ở giao lộ thời không cùng những lời đối thoại sâu sắc về vận mệnh Khaenri'ah."),
       ],
       pdf='', footer='Chương V · Màn VI — Thời Không Mà Ta Tồn Tại', side=False),
  dict(id='bckn-modau', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_modau.txt', act='Bài Ca Không Nguyệt · Mở Đầu',
       title='Đường Về Nhà', sub='Nhiệm vụ Ma Thần — Nod-Krai',
       hero='sc_bckn_modau.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Ineffa', role='Người máy hầu gái mất trí nhớ từ Nod-Krai', img='ineffa_icon.png', desc='Được Aino lắp ráp từ một lõi cổ đại và trôi dạt tới Natlan; mang trong mình nửa ý thức tách ra từ Lãnh Chúa Thứ Mười Một hai ngàn năm trước.'),
         dict(name='Chasca', role='Chiến binh Hội Hoa Vũ · Tên Cổ Vuka', img='chasca_icon.png', desc='Tiếp đón và che chở cho gia đình thương nhân Zhuoxin từ Nod-Krai cùng cô người máy Ineffa.'),
         dict(name='Ifa', role='Bác sĩ thú y Hội Hoa Vũ (cùng Cacucu)', img='ifa_icon.png', desc='Kiểm tra tình trạng cho đoàn thương nhân và đồng hành cùng chú Qucusaur trợ lý Cacucu.'),
         dict(name='Xilonen', role='Thợ rèn Tên Cổ · Con Của Tiếng Vang', img='xilonen_icon.png', desc='Đánh thức lõi cổ đại trong Ineffa và phối hợp cùng Citlali giải mã cấu trúc di tích Sảnh Tế Lễ Sắc Màu.'),
         dict(name='Citlali', role='Đại Shaman “Bà Itztli” · Chủ Nhân Gió Đêm', img='citlali_icon.png', desc='Tra cứu cổ sử về Mười Ba Lãnh Chúa Tối Cao để phanh phui cạm bẫy nhắm vào Ineffa.'),
         dict(name='Kinich · Ajaw', role='Thợ săn Dòng Dõi Vườn Treo và cộng sự', img='kinich_icon.png', desc='Nhận ủy thác tìm Ineffa cho đoàn thương nhân; Ajaw bị tra hỏi và hé lộ bản thân từng thuộc Mười Ba Lãnh Chúa Tối Cao.'),
         dict(name='Mavuika', role='Hỏa Thần của Natlan', img='mavuika_icon.png', desc='Đón nhóm Lumine và Ineffa ngoài cửa phong ấn di tích sau khi sự việc được giải quyết an toàn.'),
         dict(name='Aino · Sandrone · Varka', role='Nhân vật Nod-Krai qua ký ức & truyền âm', img='aino_icon.png', desc='Aino xuất hiện trong ký ức lắp ráp Ineffa; Sandrone truyền âm từ đội đặc nhiệm Fatui và Varka để lại thư trong hộp khóa mã.'),
         dict(name='Zhuoxin · Aamu · Adieta · Tấm Gương Bình Minh', role='Đoàn thương nhân Nod-Krai & Lãnh Chúa Thứ Mười Một', desc='Gia đình thương nhân tìm đường hoàn lương khỏi nợ Fatui và thực thể rồng cổ muốn đoạt lại lõi trong Ineffa.'),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Mở Đầu — Đường Về Nhà', side=False),
  dict(id='bckn-man1', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_man1.txt', act='Bài Ca Không Nguyệt · Màn I',
       title='Vũ Điệu Của Rừng Sương Và Sóng Tuyết', sub='Nhiệm vụ Ma Thần — Nod-Krai',
       hero='sc_bckn_man1.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Ineffa', role='Người máy mang Nguyệt Luân của Xưởng Krumkake', img='ineffa_icon.png', desc='Cùng Lumine và Paimon cập bến Thị Trấn Nasha trở về bên Aino và gia đình.'),
         dict(name='Aino', role='Thợ cơ khí thiên tài tại Xưởng Krumkake Clink-Clank', img='aino_icon.png', desc='Cô bé sáng chế ra Ineffa và các cỗ máy kỳ thú ở Thị Trấn Nasha.'),
         dict(name='Lauma', role='Vịnh Nguyệt Sứ · Thủ lĩnh Dòng Dõi Sương Nguyệt', img='lauma_icon.png', desc='Mang dòng máu bạc có khả năng trung hòa Kuuvahki, bảo vệ Đảo Hiisi và đưa ra lựa chọn công khai sự thật bầu trời giả cho tộc nhân.'),
         dict(name='Flins', role='Chiến sĩ Người Giữ Đèn (Ratnik)', img='flins_icon.png', desc='Người giữ đèn canh gác nghĩa trang phía bắc Nod-Krai, giúp đỡ nhóm Lumine bảo vệ Tủy Mặt Trăng.'),
         dict(name='Columbina', role='“Thiếu Nữ Mặt Trăng” Kuutar', img='columbina_icon.png', desc='Cựu Quan Chấp Hành thứ ba đã rời Fatui và đang ẩn cư hồi phục sức mạnh tại Sảnh Ánh Bạc.'),
         dict(name='Nefer', role='Cô chủ Hội Đồng Bí Mật', img='nefer_icon.png', desc='Người Sumeru điều hành mạng lưới tình báo sắc sảo tại Thị Trấn Nasha cùng chú mèo mun Ashru.'),
         dict(name='Jahoda', role='Nhân viên Hội Đồng Bí Mật', img='jahoda_icon.png', desc='Tự nhận là thợ săn kho báu hàng đầu, dẫn nhóm Lumine đột nhập Cục Thiết Kế Thí Nghiệm Kuuvahki.'),
         dict(name='Sandrone', role='Quan Chấp Hành thứ bảy của Fatui (“Marionette”)', img='sandrone_icon.png', desc='Đứng sau cỗ máy khổng lồ Pulonia và cục thí nghiệm Kuuvahki tại Nod-Krai.'),
         dict(name='Mualani · Kachina · Kinich · Dori · Katheryne', role='Các đồng đội Natlan tiễn đường & người quen ở Nasha', img='mualani_icon.png', desc='Mualani, Kachina và Kinich (cùng Ajaw) tiễn đoàn rời Natlan; Dori mở tiệm tại Thị Trấn Nasha và Katheryne phụ trách Hiệp Hội Nhà Mạo Hiểm.'),
         dict(name='Luonnotar · Vilemina · Aether', role='Kuuhenki, kẻ phản bội Sương Nguyệt & ảo ảnh', desc='Sinh linh Kuuhenki đồng hành bên Lumine, cựu thành viên Sương Nguyệt giao Tủy Mặt Trăng cho Fatui và bóng ma giả dạng Aether.'),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Màn I — Vũ Điệu Của Rừng Sương Và Sóng Tuyết', side=False),
  dict(id='bckn-man2', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_man2.txt', act='Bài Ca Không Nguyệt · Màn II',
       title='Bi Ca Của Cát Bụi Và Ánh Đèn', sub='Nhiệm vụ Ma Thần — Nod-Krai',
       hero='sc_bckn_man2.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Flins', role='Ratnik của Người Giữ Đèn', img='flins_icon.png', desc='Đối mặt bóng ma quá khứ tại Nghĩa Trang Đêm Cuối và hé lộ thân phận là một fae ẩn mình từ thời cổ đại Snezhnaya.'),
         dict(name='Columbina', role='“Thiếu Nữ Mặt Trăng” Kuutar', img='columbina_icon.png', desc='Hồi phục dần trong Sảnh Trăng Bạc và sát cánh ngăn chặn âm mưu của Thợ Săn Ánh Trăng.'),
         dict(name='Lauma', role='Vịnh Nguyệt Sứ Dòng Dõi Sương Nguyệt', img='lauma_icon.png', desc='Điều phối lực lượng Đảo Hiisi ứng phó các dị tượng của Cuộc Săn Hoang Dã.'),
         dict(name='Nefer', role='Chủ nhân Hội Đồng Bí Mật', img='nefer_icon.png', desc='Cung cấp tình báo về phi thuyền thất lạc và nguồn gốc cơn bão dị tượng tại Thị Trấn Nasha.'),
         dict(name='Jahoda', role='Trợ thủ của Nefer tại Hội Đồng Bí Mật', img='jahoda_icon.png', desc='Tháo vát hỗ trợ điều tra các đầu mối tại Thị Trấn Nasha.'),
         dict(name='Aino · Ineffa', role='Chủ nhân và người máy Xưởng Krumkake', img='aino_icon.png', desc='Chế tạo khẩu đại pháo và robot kiểm tra Birgitta góp phần đẩy lùi làn sóng tấn công.'),
         dict(name='Sandrone', role='Quan Chấp Hành thứ bảy Fatui', img='sandrone_icon.png', desc='Xuất hiện cùng cỗ máy Pulonia cản bước Rerir ngay tại khu vực cục thí nghiệm.'),
         dict(name='Varka', role='Kỵ Sĩ Bắc Phong · Đại Đội Trưởng Đội Kỵ Sĩ Tây Phong', img='varka_icon.png', desc='Trực tiếp xuất hiện ở đoạn kết đối đầu Rerir để giải nguy cho nhóm Lumine.'),
         dict(name='Rerir', role="“Thợ Săn Ánh Trăng” · Một trong Năm Tội Nhân Khaenri'ah", img='wildhunt_icon.png', desc='Bản thể đứng sau Cuộc Săn Hoang Dã và các bóng ma săn tìm Tủy Mặt Trăng.'),
         dict(name='Aether · Dori · Luonnotar', role='Ký ức phi thuyền, thương nhân & tiểu tinh linh ánh trăng', img='dori_icon.png', desc='Aether hiện qua mảnh ký ức phi thuyền hạ cánh; Dori xuất hiện ở Nasha và Luonnotar dẫn lối cho Lumine.'),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Màn II — Bi Ca Của Cát Bụi Và Ánh Đèn', side=False),
  dict(id='bckn-man3', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_man3.txt', act='Bài Ca Không Nguyệt · Màn III',
       title='Vương Quốc Không Tồn Tại', sub='Nhiệm vụ Ma Thần — Nod-Krai',
       hero='nefer_splash.png',
       cast=[LUMINE, PAIMON,
         dict(name='Nefer', role='Chủ nhân Hội Đồng Bí Mật · Quản lý Mạng Lưới Tình Báo Bắc Đại Lục', img='nefer_icon.png', desc="Thực hiện nghi thức bí mật thâm nhập mảnh vỡ ký ức Khaenri'ah của Rerir để tìm điểm yếu đối phó."),
         dict(name='Varka', role='Đại Đội Trưởng Đội Kỵ Sĩ Tây Phong', img='varka_icon.png', desc='Trở về từ Amsvartnir kịp lúc giải cứu cả nhóm và điều phối chiến dịch tác chiến từ căn cứ bí mật.'),
         dict(name='Columbina', role='“Thiếu Nữ Mặt Trăng” Kuutar', img='columbina_icon.png', desc='Bị Rerir truy sát gắt gao và tìm cách thu hồi sức mạnh từ Tủy Mặt Trăng Hồng Nguyệt.'),
         dict(name='Arlecchino', role='Quan Chấp Hành thứ tư của Fatui (“The Knave”)', img='arlecchino_icon.png', desc='Mang huyết mạch Triều Đại Xích Nguyệt, mở cổng không gian Hồng Nguyệt giải cứu mọi người và tạm giữ Tủy Mặt Trăng Hồng Nguyệt.'),
         dict(name='Sandrone', role='Quan Chấp Hành thứ bảy của Fatui', img='sandrone_icon.png', desc='Chuyển lời của Columbina tới Arlecchino và điều khiển Pulonia cùng đội B.O.S.C.O. cản bước Cuộc Săn Hoang Dã.'),
         dict(name='Lauma · Flins · Jahoda', role='Vịnh Nguyệt Sứ, Người Giữ Đèn và trợ thủ Hội Đồng Bí Mật', img='lauma_icon.png', desc='Tham gia nghi thức đọc ký ức Rerir và đánh lạc hướng đội quân Cuộc Săn Hoang Dã.'),
         dict(name='Aino · Ineffa', role='Nhóm Xưởng Krumkake Clink-Clank', img='ineffa_icon.png', desc='Chế tạo mồi nhử đánh lạc hướng Rerir và lên đường điều tra bí ẩn ở Amsvartnir.'),
         dict(name='Lyney · Lynette · Freminet', role='Anh em Căn Nhà Hơi Ấm', img='lyney_icon.png', desc='Được Arlecchino phái tới Cục Thiết Kế Thí Nghiệm hỗ trợ Sandrone sửa chữa thiết bị.'),
         dict(name='Dori', role='Đại thương nhân Sangemah Bay', img='dori_icon.png', desc='Cho Nefer mượn món bảo vật phòng thân đặc biệt để tiến hành nghi thức thâm nhập ký ức.'),
         dict(name='Rerir', role="“Thợ Săn Ánh Trăng” · Cựu đặc vụ Khaenri'ah", img='wildhunt_icon.png', desc='Truy sát Columbina, đồng thời lộ rõ quá khứ từng săn giết Tàn Dư Xích Nguyệt dưới trướng Hắc Vương Irmin.'),
         dict(name='Tholindis · Dainsleif · Vedrfolnir', role="Nhân vật trong mảnh ký ức Khaenri'ah", img='dainsleif_icon.png', desc='Vị hôn thê Tholindis tại Viện Bí Ẩn cùng anh em Dainsleif và “Tiên Tri” Vedrfolnir xuất hiện trong ký ức của Rerir.'),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Màn III — Vương Quốc Không Tồn Tại', side=False),
  dict(id='bckn-man4', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_man4.txt', act='Bài Ca Không Nguyệt · Màn IV',
       title='Bi Ca Ánh Trăng Tàn', sub='Nhiệm vụ Ma Thần — Nod-Krai',
       hero='nc_nodkrai_moonbright.png',
       cast=[LUMINE, PAIMON,
         dict(name='Nefer', role='Chủ nhân Hội Đồng Bí Mật', img='nefer_icon.png', desc='Cùng nhóm Lumine tìm cách đẩy Rerir vào vực thẳm không gian, đồng thời đối diện lại quá khứ tuổi thơ ở tộc Shimti sa mạc Sumeru.'),
         dict(name='Albedo', role='Giả Kim Thuật Sĩ · Đội Trưởng Đội Điều Tra', img='albedo_icon.png', desc='Phối hợp giải thích cơ chế không gian và hỗ trợ triển khai mặt trận tổng lực tại Nod-Krai.'),
         dict(name='Durin', role='Thiếu niên mang sức mạnh ma long', img='durin_icon.png', desc='Từ Mondstadt tới Nod-Krai sát cánh cùng Albedo đối phó dị tượng Vực Sâu.'),
         dict(name='Dainsleif', role="“Kẻ Nhặt Cành” · Cựu Đội Trưởng Cận Vệ Hoàng Gia Khaenri'ah", img='dainsleif_icon.png', desc='Góp mặt mở cổng không gian giam giữ Rerir và trực tiếp đối chiếu ký ức với những Tội Nhân năm xưa.'),
         dict(name='Varka · Flins · Lauma · Jahoda', role='Liên quân bảo vệ Nod-Krai', img='varka_icon.png', desc='Phối hợp giữ phòng tuyến tại Thị Trấn Nasha và Sương Nguyệt Phường trong chiến dịch đánh bại Thợ Săn Ánh Trăng.'),
         dict(name='Columbina · Arlecchino · Sandrone', role='Nguyệt Thần và hai Quan Chấp Hành Fatui', img='columbina_icon.png', desc='Cùng liên thủ mở phong ấn và phối hợp với nhóm Lumine đánh bật cuộc tấn công của Rerir.'),
         dict(name='Aino · Ineffa · Dori', role='Đồng minh hậu cần & thương hội', img='aino_icon.png', desc='Hỗ trợ vật tư, thiết bị và công tác chiến trường trong trận chiến cuối cùng với Rerir.'),
         dict(name='Rerir · Tholindis', role='Thợ Săn Ánh Trăng và vị hôn thê (ký ức)', img='wildhunt_icon.png', desc="Trận quyết chiến khép lại câu chuyện bi kịch của Rerir cùng mảnh ký ức cuối về Tholindis tại Khaenri'ah."),
         dict(name='Vedrfolnir · Rhinedottir', role="Các Tội Nhân Khaenri'ah (ký ức)", desc="Cùng Surtalogi và Hroptatyr hiện diện trong ký ức bàn cờ tại Khaenri'ah."),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Màn IV — Bi Ca Ánh Trăng Tàn', side=False),
  dict(id='bckn-man5', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_man5.txt', act='Bài Ca Không Nguyệt · Màn V',
       title='Thơ Dạ Hành Cực Bắc', sub='Nhiệm vụ Ma Thần — Nod-Krai',
       hero='sc_bckn_man5.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Columbina', role='“Thiếu Nữ Mặt Trăng” Kuutar', img='columbina_icon.png', desc='Ngày càng suy yếu vì bị thế giới bài xích do không có tên thật, lặng lẽ quan sát cuộc sống ở Nasha trước nghi thức mở cổng Hyperborea.'),
         dict(name='Alice', role='Thành viên Hội Ma Nữ · Mẹ của Klee', desc='Lần đầu lộ diện bằng thân xác thật tại Thị Trấn Nasha, lý giải hiện tượng “Ba Mặt Trăng Thẳng Hàng” và hai điều kiện cứu Columbina.'),
         dict(name='Nicole', role='Ma Nữ “N” · Thành viên Hội Ma Nữ (Thiên Sứ cổ đại)', img='nicole_icon.png', desc='Giao tiếp trực tiếp trong tâm trí và dẫn dắt nghi thức cộng hưởng Kuuvahki mở cánh cổng Hyperborea.'),
         dict(name='Lauma', role='Vịnh Nguyệt Sứ Dòng Dõi Sương Nguyệt', img='lauma_icon.png', desc='Chuẩn bị Đêm Cầu Nguyệt, trao đổi tư liệu Hyperborea với Nefer tìm tên thật cho Kuutar và tham gia nghi thức mở cổng.'),
         dict(name='Varka', role='Đại Đội Trưởng Đội Kỵ Sĩ Tây Phong', img='varka_icon.png', desc='Điều phối lễ hội, cùng Lumine và Lauma điều tra hư ảnh phi thuyền tại Bãi Cát Sao và kết nối các phe phái.'),
         dict(name='Kẻ Lang Thang', role='Driyosh Học Viện Vahumana (“Nón Tròn”)', img='wanderer_icon.png', desc='Tới Nod-Krai bổ sung hồ sơ điều tra về Dottore và lần đầu kể cho Durin nghe về xuất thân của mình.'),
         dict(name='Durin · Albedo', role='Hai đại diện Hội Ma Nữ & Kỵ Sĩ Tây Phong', img='durin_icon.png', desc='Điều tra các hư ảnh Vực Sâu; Durin vận dụng sức mạnh phá vỡ vòng lặp hư ảnh cổ đại.'),
         dict(name='Flins · Nefer · Jahoda', role='Người Giữ Đèn và Hội Đồng Bí Mật', img='flins_icon.png', desc='Flins tiết lộ từng chứng kiến thảm họa 500 năm trước; Nefer và Jahoda khám phá Bãi Cát Sao và thử nghiệm Kuuvahki.'),
         dict(name='Arlecchino · Sandrone', role='Hai Quan Chấp Hành Fatui', img='arlecchino_icon.png', desc='Tiết lộ Nữ Hoàng đã triệu hồi Dottore; Arlecchino tình nguyện làm người thứ ba hoàn thành nghi thức mở cổng.'),
         dict(name='Aino · Ineffa · Katheryne · Luonnotar', role='Cư dân Nasha & Kuuhenki', img='ineffa_icon.png', desc='Hỗ trợ thử nghiệm Kuuvahki và chăm sóc nhóm Lumine suốt ba ngày nhịn ăn truyền năng lượng.'),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Màn V — Thơ Dạ Hành Cực Bắc', side=False),
  dict(id='bckn-man6', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_man6.txt', act='Bài Ca Không Nguyệt · Màn VI',
       title='Ánh Trăng Tan Trong Sương Sớm', sub='Nhiệm vụ Ma Thần — Nod-Krai',
       hero='sc_bckn_man6.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Columbina', role='Columbina Hyposelenia · Nguyệt Thần Sương Nguyệt', img='columbina_icon.png', desc='Tìm lại được tên thật từ những người bạn tại di tích Hyperborea, tận hưởng Đêm Cầu Nguyệt rồi nhảy vào Cổng Mặt Trăng ngăn Dottore.'),
         dict(name='Dottore', role='Quan Chấp Hành thứ hai của Fatui', img='dottore_icon.png', desc='Lợi dụng biến số Hyperborea dựng nên “vầng trăng giả”, phục kích bắt giữ Columbina và đoạt Tủy Mặt Trăng.'),
         dict(name='Nicole', role='Ma Nữ “N” · Thiên Sứ cổ đại', img='nicole_icon.png', desc='Giảng giải lịch sử Trận Chiến Tang Hỏa và Ba Nữ Thần Mặt Trăng, đồng thời mở gian hàng dưới hình dạng Dodoco.'),
         dict(name='Alice · Barbeloth', role='Hai Ma Nữ Hội Ma Nữ (Dodoco)', desc='Xuất hiện dưới hình dạng Dodoco trong Đêm Cầu Nguyệt; Alice gửi tin cảnh báo về âm mưu “biến số” từ biên giới Teyvat còn Barbeloth bói bốn lá Thánh Bài Ánh Trăng.'),
         dict(name='Arlecchino', role='Quan Chấp Hành Fatui (“Peruere”)', img='arlecchino_icon.png', desc='Sát cánh tìm tên cho Columbina và tuyên bố sẵn sàng lấy tên thật “Peruere” nghênh chiến Dottore.'),
         dict(name='Sandrone', role='Quan Chấp Hành Fatui (“Marionette”)', img='sandrone_icon.png', desc='Âm thầm dự Đêm Cầu Nguyệt, so tài cùng Columbina và bộc lộ cảm xúc khi nhận kỷ vật Hội Narzissenkreuz.'),
         dict(name='Varka · Albedo · Durin · Kẻ Lang Thang', role='Nhóm điều tra từ Mondstadt & Sumeru', img='varka_icon.png', desc='Varka điều phối phòng tuyến chống Dottore; Durin và Kẻ Lang Thang gặp lại đồ chơi Simulanka trước khi Kẻ Lang Thang vạch trần thủ đoạn trăng giả.'),
         dict(name='Lauma · Flins · Nefer · Jahoda', role='Các đồng minh Nod-Krai', img='lauma_icon.png', desc='Chuẩn bị Đêm Cầu Nguyệt, tìm kiếm tung tích Columbina và thu thập tình báo chống Dottore.'),
         dict(name='Aino · Ineffa · Dori · Luonnotar', role='Cư dân Nasha, thương nhân & Kuuhenki', img='aino_icon.png', desc='Phụ trách các gian hàng Đêm Cầu Nguyệt và nghiên cứu lại phương thức của Dottore sau biến cố.'),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Màn VI — Ánh Trăng Tan Trong Sương Sớm', side=False),
  dict(id='bckn-man7', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_man7.txt', act='Bài Ca Không Nguyệt · Màn VII',
       title='Nếu Một Đêm Đông, Có Vị Lữ Khách', sub='Nhiệm vụ Ma Thần — Nod-Krai',
       hero='nc_nodkrai_snow.png',
       cast=[LUMINE, PAIMON,
         dict(name='Columbina', role='Columbina Hyposelenia (trong dòng thời gian ngược)', img='columbina_icon.png', desc='Mắc kẹt trong hình bóng phản chiếu mặt trăng trôi ngược về quá khứ, âm thầm cứu Đảo Hiisi, gửi manh mối cho bạn bè và tạo ra Luonnotar.'),
         dict(name='Dottore', role='Quan Chấp Hành thứ hai Fatui', img='dottore_icon.png', desc='Chiếm giữ Tủy Mặt Trăng, lập vùng năng lượng thí nghiệm và giam giữ Lumine để thực hiện âm mưu vượt số mệnh.'),
         dict(name='Kẻ Lang Thang', role='“Nón Tròn” · Học giả Sumeru', img='wanderer_icon.png', desc='Cùng Albedo và Durin thâm nhập vùng năng lượng và tự tay phá vỡ kết giới cứu Lumine thoát khỏi tay Dottore.'),
         dict(name='Albedo · Durin', role='Giả Kim Thuật Sĩ và bạn đồng hành', img='albedo_icon.png', desc='Phân tích Lãnh Địa Ánh Sáng và dùng sức mạnh Hỏa cùng Vực Sâu phá vỡ rào chắn năng lượng.'),
         dict(name='Arlecchino', role='Quan Chấp Hành thứ tư Fatui', img='arlecchino_icon.png', desc='Nhận mật chỉ từ Nữ Hoàng Băng cho phép tự quyết tiêu diệt kẻ phản bội Dottore.'),
         dict(name='Sandrone', role='Quan Chấp Hành thứ bảy Fatui', img='sandrone_icon.png', desc='Cùng Albedo nghiên cứu mô thức thế giới dựa trên ghi chép của Alain Guillotin và Rene de Petrichor.'),
         dict(name='Childe', role='Quan Chấp Hành thứ mười một Fatui', img='childe_icon.png', desc='Mang chỉ dụ của Nữ Hoàng Băng từ Snezhnaya tới tiếp nhận người dân Nod-Krai đi lánh nạn.'),
         dict(name='Varka · Lauma · Nefer · Flins · Jahoda · Illuga', role='Lực lượng bảo vệ và sơ tán Nod-Krai', img='illuga_icon.png', desc='Giữ vững Thị Trấn Nasha, giải mã mật thư của Columbina và phối hợp sơ tán dân chúng sang Natlan.'),
         dict(name='Aino · Ineffa · Dori · Nicole · Barbeloth', role='Đồng minh kỹ thuật, liên lạc & Hội Ma Nữ', img='nicole_icon.png', desc='Aino và Ineffa giao “Vịt Bình Tĩnh” hỗ trợ; Dori về Sumeru báo tin Nahida; Nicole cứu Nefer qua Bộ Liên Lạc Dodoco.'),
         dict(name='Aether · Luonnotar · Rerir', role='Hình ảnh ý thức, Kuuhenki & ký ức quá khứ', img='aether_icon.png', desc='Aether hiện im lặng cạnh Lumine trong tầng ý thức; Luonnotar dẫn đường và Rerir thoáng hiện trong ký ức Bãi Cát Sao.'),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Màn VII — Nếu Một Đêm Đông, Có Vị Lữ Khách', side=False),
  dict(id='bckn-man8', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_man8.txt', act='Bài Ca Không Nguyệt · Màn VIII',
       title='Mặt Trăng Thực Sự', sub='Nhiệm vụ Ma Thần — Nod-Krai',
       hero='nc_char_columbina.png',
       cast=[LUMINE, PAIMON,
         dict(name='Columbina', role='Tam Nguyệt Nữ Thần duy nhất của Teyvat', img='columbina_icon.png', desc='Đi ngược thời không gặp Tam Nguyệt Nữ Thần nguyên thủy, tiếp nhận quyền năng ba mặt trăng để tái lâm đánh bại Dottore và mở lối phi thuyền.'),
         dict(name='Sandrone', role='Quan Chấp Hành thứ bảy Fatui (“Marionette”)', img='sandrone_icon.png', desc='Hoàn thành thuật thức thế giới giấu trong Pulonia và dũng cảm đỡ đòn chí mạng thay Lumine trong trận chiến cuối.'),
         dict(name='Kẻ Lang Thang', role='“Nón Tròn”', img='wanderer_icon.png', desc='Tự nguyện rút lõi Cây Thế Giới của bản thân để vận hành thuật thức thế giới, sau chiến thắng hồi phục và trở về Sumeru.'),
         dict(name='Dottore', role='Quan Chấp Hành thứ hai Fatui (“Kẻ Dị Giáo Của Mặt Trăng Giả”)', img='dottore_boss_icon.png', desc='Bị Columbina cùng Lumine, Flins, Lauma và Nefer hợp lực đánh bại và tan biến tại không gian mặt trăng giả.'),
         dict(name='Arlecchino', role='Quan Chấp Hành thứ tư Fatui', img='arlecchino_icon.png', desc='Cùng Varka và Nicole kéo Sương Nguyệt xuyên qua bầu trời giả, nhận lại Tủy Mặt Trăng Hồng Nguyệt và khởi hành về Fontaine.'),
         dict(name='Nefer · Lauma · Flins · Jahoda · Illuga', role='Các đại diện Liên Minh Nod-Krai', img='nefer_icon.png', desc='Phối hợp đánh bại Dottore, bảo vệ Thị Trấn Nasha và cùng đại diện Người Giữ Đèn Illuga thành lập Liên Minh Nod-Krai.'),
         dict(name='Varka · Albedo · Durin · Nicole', role='Kỵ Sĩ Tây Phong & Thiên Sứ Hội Ma Nữ', img='varka_icon.png', desc='Kéo Sương Nguyệt trở về, chuyển giao ước bảo vệ Nod-Krai và bảo toàn thị trấn sau thảm họa.'),
         dict(name='Aino · Ineffa · Luonnotar', role='Cư dân Nasha & phần linh hồn kết nối của Columbina', img='ineffa_icon.png', desc='Phân phát thực phẩm sau trận chiến và hoàn thành cầu nối đưa Columbina trở về thực tại.'),
         dict(name='Rerir · Tholindis', role='Hai linh hồn nơi nhà tù ánh trăng (ký ức)', img='wildhunt_icon.png', desc='Rerir đã dọn chướng ngại mở đường cho Columbina, còn Tholindis nhắn gửi lời tha thứ cho anh từ quá khứ.'),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Màn VIII — Mặt Trăng Thực Sự', side=False),
  dict(id='bckn-man9', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_man9.txt', act='Bài Ca Không Nguyệt · Màn IX',
       title='Thân Thổ Tiêu Tan, Ngũ Uẩn Chuyển Biến', sub='Nhiệm vụ Ma Thần — Bài Ca Không Nguyệt · Sumeru',
       hero='sc_bckn_man9.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Collei', role='Kiểm lâm Rừng Avidya', img='collei_icon.png', desc='Nhận điềm báo kỳ lạ khi Thành Sumeru đảo lộn trong mộng cảnh, dùng lời thơ Hoa Thần trấn tĩnh bầy Trấn Linh và biết bí mật mảnh tàn dư trong cơ thể.'),
         dict(name='Nahida', role='Tiểu Vương Kusanali · Thảo Thần', img='nahida_icon.png', desc='Kết nối trực tiếp với Cây Thế Giới đến kiệt sức hôn mê, được đưa tới Trái Tim Ốc Đảo của Apep trị liệu.'),
         dict(name='Kẻ Lang Thang', role='“Nón Tròn”', img='wanderer_icon.png', desc='Phối hợp phân tích dữ liệu rối loạn của Cây Thế Giới và hộ tống đoàn sơ tán về sa mạc.'),
         dict(name='Tighnari · Cyno · Alhaitham · Kaveh · Sethos · Faruzan', role='Nhóm điều tra Giáo Viện & Ngôi Đền Im Lặng', img='sethos_icon.png', desc='Tighnari và Alhaitham vạch kế hoạch khôi phục Akasha từ Aaru; Sethos, Cyno, Kaveh và Faruzan cùng giữ vững phòng tuyến Sumeru.'),
         dict(name='Dehya · Nilou · Dori · Jeht · Rahman', role='Các đồng minh sa mạc và Thành Sumeru', img='dehya_icon.png', desc='Jeht (cùng Benben) giải cứu nhóm Lumine dưới Thành Gurabad; Dehya, Nilou, Dori và Rahman cùng chung tay bảo vệ Làng Aaru và đồng đội.'),
         dict(name='Naphis và Cyrus', role='Đại Hiền Giả mới & Hiền Giả Giáo Viện', desc='Điều phối sơ tán Thành Sumeru và hỗ trợ nhóm Lumine thâm nhập tàn tích cổ đại.'),
         dict(name='Nicole · Nefer', role='Thiên Sứ Hội Ma Nữ và chủ Hội Đồng Bí Mật', img='nefer_icon.png', desc='Nicole truyền âm chỉ dẫn Collei trước khi trực tiếp lộ diện đưa Nefer tới tiếp ứng cho Sumeru (cùng Jahoda trong hồi tưởng).'),
         dict(name='Apep', role='Thảo Long Vương cổ đại của Sumeru', img='apep_icon.png', desc='Nhận lời đền ân dùng Trái Tim Ốc Đảo cứu chữa cho Tiểu Vương Kusanali.'),
         dict(name='Thoth · Heryshaf · Sobek · Liloupar', role='Bảy Trụ Cột của Vua Deshret & Trấn Linh cổ đại', desc='Ba cổ thần trong Aaru bỏ phiếu mở cổng cứu trợ, còn Liloupar tỉnh giấc dẹp yên bão cát Trấn Linh tại Gurabad.'),
         dict(name='Katheryne · Capitano', role='Hiệp Hội Nhà Mạo Hiểm & ký ức Natlan', img='katheryne_icon.png', desc='Katheryne trao thư của Collei tại Nod-Krai; Capitano thoáng hiện trong hồi ức của Lumine.'),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Màn IX — Thân Thổ Tiêu Tan, Ngũ Uẩn Chuyển Biến', side=False),
  dict(id='bckn-man10', arc='Bài Ca Không Nguyệt · Nod-Krai', src='bckn_man10.txt', act='Bài Ca Không Nguyệt · Màn X',
       title='Vô Vàn Con Đường, Biến Chuyển Và Tan Rã', sub='Nhiệm vụ Ma Thần — Bài Ca Không Nguyệt · Sumeru',
       hero='sc_bckn_man10.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Nahida', role='Tiểu Vương Kusanali · Thảo Thần', img='nahida_icon.png', desc='Bình phục để đối mặt trực diện cuộc thí nghiệm của Dottore nhắm vào Cây Thế Giới và vận mệnh Teyvat.'),
         dict(name='Kẻ Lang Thang', role='“Nón Tròn” · Truyền nhân Sumeru', img='wanderer_icon.png', desc='Đối đầu trực diện với Zandik — Dottore để thanh toán món nợ hàng trăm năm từ Tatarasuna tới Cây Thế Giới.'),
         dict(name='Alhaitham · Kaveh · Cyno · Tighnari · Collei · Sethos · Faruzan · Layla', role='Đội ngũ học giả và chiến binh Sumeru', img='layla_icon.png', desc='Hợp sức bảo vệ Cây Thế Giới và ngăn chặn sự ăn mòn lan rộng khắp lục địa Sumeru.'),
         dict(name='Dehya · Candace · Dunyarzad · Dori · Nefer · Jeht · Rahman · Haypasia', role='Các đồng minh thành thị, sa mạc và Hội Đồng Bí Mật', img='dehya_icon.png', desc='Giữ vững hậu phương từ Thành Sumeru tới Làng Aaru trong chiến dịch giải cứu Cây Thế Giới.'),
         dict(name='Naphis và Cyrus', role='Đại Hiền Giả và Hiền Giả Giáo Viện', desc='Phối hợp kích hoạt hệ thống phòng thủ tri thức cùng các học giả Giáo Viện.'),
         dict(name='Apep · Thoth · Heryshaf · Sobek · Liloupar', role='Thảo Long Vương, Thất Trụ Deshret và Trấn Linh', img='apep_icon.png', desc='Cùng nhóm Aranara và Pari Sorush đồng loạt đứng lên bảo vệ đất thánh Sumeru.'),
         dict(name='Mavuika · Albedo · Sucrose · Amber', role='Hỏa Thần Natlan và nhóm Mondstadt', img='mavuika_icon.png', desc='Ứng chiến và dõi theo biến động toàn cầu khi Cây Thế Giới bị uy hiếp (cùng hồi ức về Mualani, Kachina, Varesa và đồng đội Natlan).'),
         dict(name='Nicole · Ronova · Istaroth · Naberius', role='Thiên Sứ Hội Ma Nữ và Các Chấp Chính Thiên Lý', img='nicole_icon.png', desc='Nicole tiếp ứng từ bên ngoài trong khi các Chấp Chính Thiên Lý hiện chiếu quan sát biến cố Cây Thế Giới.'),
         dict(name='Dottore · Pantalone', role='Hai Quan Chấp Hành Fatui', img='dottore_moon_icon.png', desc='Dottore (Zandik) thực hiện tham vọng chạm tới Ngai Thần và Cây Thế Giới với sự hậu thuẫn của Pantalone.'),
       ],
       pdf='', footer='Bài Ca Không Nguyệt · Màn X — Vô Vàn Con Đường, Biến Chuyển Và Tan Rã', side=False),
  dict(id='c7-man1', arc='Chương VII · Snezhnaya', src='c7_man1.txt', act='Chương VII · Màn I',
       title='Đất Nước Của Tuyết Không Được Thần Thương Yêu', sub='Nhiệm vụ Ma Thần — Snezhnaya',
       hero='sc_c7_man1.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Mắt Xám', role='Mắt Graeae · Tạo vật cổ đại từ Hyperborea', desc='Bảo vật đồng hành mới giúp Lumine giải mã dị tượng và bí mật trong vùng băng tuyết Snezhnaya.'),
         dict(name='Columbina · Luonnotar', role='Tam Nguyệt Nữ Thần & tiểu tinh linh Kuuhenki', img='columbina_icon.png', desc='Tiễn chân Lumine và Paimon từ Nod-Krai lên đường tiến vào lục địa Snezhnaya.'),
         dict(name='Childe', role='Quan Chấp Hành thứ mười một · Nghị sĩ Veche', img='childe_icon.png', desc='Đón tiếp Lumine tại Snezhnograd và tham dự phiên họp căng thẳng của Hội Đồng Snezhnograd Veche.'),
         dict(name='Pierro · Pulcinella · Sandrone · Pantalone', role='Ban lãnh đạo Fatui tại Veche', desc='Quan Thống Lĩnh Pierro cùng Quan Chấp Hành thứ năm Pulcinella (người chủ trì Veche), thứ bảy Sandrone và thứ chín Pantalone điều phối cục diện chính trị Snezhnaya.'),
         dict(name='Valeriy', role='Thiếu tá Đội Nhiệm Vụ Đặc Biệt Cục Khí Tài', img='valeriy_icon.png', desc='Chỉ huy đội đặc nhiệm Cục Khí Tài tiếp xúc và theo dõi hoạt động của nhóm Lumine tại Snezhnograd.'),
         dict(name='Odette', role='Vũ công ba lê kiêm thành viên Fatui', img='odette_icon.png', desc='Ngôi sao sân khấu Nhà Hát Korolevskiy và thành viên bí mật của tổ chức Rokot mang bí danh “Lelek”.'),
         dict(name='Vodyanitsa', role='Nữ ca sĩ giọng cao thuộc tộc thủy yêu', img='vodyanitsa_icon.png', desc='Thành viên tổ chức Rokot hợp tác điều tra những biến cố băng tuyết ở Snezhnaya.'),
         dict(name='Alyosha', role='Thợ săn từ vùng biên giới Sretomorozsk', img='alyosha_icon.png', desc='Thành viên tổ chức Rokot dẫn đường cùng chú chó săn Tugarin vượt qua vùng bão tuyết.'),
         dict(name='Mitya', role='Nhà nghiên cứu năng lượng · Hiệp Hội Năng Lượng', img='mitya_icon.png', desc='Chuyên gia nghiên cứu năng lượng trẻ tuổi cộng tác giải mã hiện tượng bất thường quanh Cục Khí Tài.'),
         dict(name='Polonsky · Arapov · Akvilina · Chugunov', role='Đại biểu Veche, chủ xưởng và cư dân Snezhnaya', desc='Các nhân chứng và thành viên bộ máy hành chính tại Snezhnograd cùng làng Sretomorozsk.'),
       ],
       pdf='', footer='Chương VII · Màn I — Đất Nước Của Tuyết Không Được Thần Thương Yêu', side=False),
  dict(id='c7-man2', arc='Chương VII · Snezhnaya', src='c7_man2.txt', act='Chương VII · Màn II',
       title='Dạ Khúc Của Những Linh Hồn Đã Chết', sub='Nhiệm vụ Ma Thần — Snezhnaya',
       hero='sc_c7_man2.jpg',
       cast=[LUMINE, PAIMON,
         dict(name='Odette', role='Vũ công hàng đầu Nhà Hát Korolevskiy (“Lelek”)', img='odette_icon.png', desc='Cùng Lumine mắc kẹt trong trận bão tuyết cô lập tại nhà hát và tìm ra sự thật về những linh hồn đã khuất.'),
         dict(name='Vodyanitsa', role='Ca sĩ giọng cao tộc fae · thành viên Rokot', img='vodyanitsa_icon.png', desc='Bảo vệ nhóm bằng tiếng hát kỳ dị và đối diện với nỗi ám ảnh gia tộc giữa nhà hát phong tỏa.'),
         dict(name='Alyosha', role='Thợ săn làng Alatyr và nhân viên nhà hát', img='alyosha_icon.png', desc='Người đồng hành âm thầm ở bên nhóm Lumine suốt các màn điều tra giữa trận bão tuyết cô lập.'),
         dict(name='Valeriy', role='Thiếu tá Đội Nhiệm Vụ Đặc Biệt Cục Khí Tài', img='valeriy_icon.png', desc='Dẫn đầu lực lượng điều tra vụ án trong Nhà Hát Korolevskiy bất chấp xung đột lợi ích phe phái.'),
         dict(name='Mitya', role='Chuyên gia Hiệp Hội Năng Lượng', img='mitya_icon.png', desc='Phân tích dị tượng băng giá và thiết bị kỳ lạ gây phong tỏa nhà hát.'),
         dict(name='Ronova', role='Chấp Chính Của Cái Chết', desc='Hiện thân giữa biến cố bão tuyết tại Nhà Hát Korolevskiy ở hồi kết.'),
         dict(name='Childe · Pierro · Signora · Arlecchino', role='Các lãnh đạo và Quan Chấp Hành Fatui', img='childe_icon.png', desc='Childe (cùng em gái Tonia) và Pierro xuất hiện tại Snezhnograd; Signora và Arlecchino hiện lên trong hồi ức bên phần mộ Rosalyne.'),
         dict(name='Nữ Hoàng Băng Giá · Vesna · Danica', role='Nữ Hoàng Snezhnaya, tư lệnh Druzhna và hầu gái trưởng', img='vesna_icon.png', desc='Xuất hiện cùng đội hộ vệ Druzhna trong phân đoạn kết khép lại bí mật nhà hát.'),
         dict(name='Chugunov · “Tonia” (Ptashka) · Shram', role='Chủ xưởng và những linh hồn quá khứ', desc='Các nạn nhân và linh hồn mắc kẹt suốt nhiều thế kỷ từ Chứng Sương Thực và cuộc nội chiến năm xưa.'),
       ],
       pdf='', footer='Chương VII · Màn II — Dạ Khúc Của Những Linh Hồn Đã Chết', side=False),
  dict(id='c7-man3', arc='Chương VII · Snezhnaya', src='c7_man3.txt', act='Chương VII · Màn III',
       title='Đêm Trắng Như Vừa Tỉnh Mộng', sub='Nhiệm vụ Ma Thần — Snezhnaya',
       hero='nc_snezhnaya_queen.png',
       cast=[LUMINE, PAIMON,
         dict(name='Anastasya', role='Nữ Hoàng Băng Giá của Snezhnaya (Ma Thần Vassaga)', img='anastasya_icon.png', desc='Chính thức gặp gỡ Lumine trong bối cảnh biến động triều chính, phơi bày những mâu thuẫn giữa lý tưởng cứu thế và hiện thực khắc nghiệt.'),
         dict(name='Pierro · Childe · Pulcinella · Pantalone · Sandrone', role='Quan Thống Lĩnh và các Quan Chấp Hành Fatui', img='childe_icon.png', desc='Tham gia đối chất trong nội bộ triều đình và Cục Khí Tài Snezhnaya.'),
         dict(name='Danica', role='Trưởng nữ hầu hoàng gia Cung Điện Zapolyarny', desc='Người cận kề hầu hạ Nữ Hoàng Anastasya và thực thi các mệnh lệnh mật tại cung điện.'),
         dict(name='Vesna', role='Tư lệnh đội hộ vệ Druzhna · fae tộc Vila', img='vesna_icon.png', desc='Chỉ huy đội Druzhna trung thành tuyệt đối bảo vệ Nữ Hoàng và trật tự đế chế.'),
         dict(name='Alyosha · Odette · Vodyanitsa · Mitya · Mắt Xám', role='Nhóm đồng minh Snezhnograd & tạo vật Hyperborea', img='odette_icon.png', desc='Phối hợp cùng Lumine mở đường qua tuyến đường sắt Đêm Trắng trong làn vây của Oprichniki.'),
         dict(name='Lyney · Lynette · Freminet', role='Ba anh em Căn Nhà Hơi Ấm', img='lyney_icon.png', desc='Hoạt động âm thầm tại Snezhnaya để hỗ trợ Lumine trong chiến dịch giải cứu và thu thập thông tin.'),
         dict(name='Ronova · Rhinedottir · Venti', role='Các Chấp Chính Thiên Lý và ký ức Phong Thần', desc='Ronova hiện qua ký ức; Rhinedottir (Chấp Chính Của Sự Sống mang Naberius) trực tiếp đối diện tình thế cùng tiếng vang ký ức về Venti.'),
       ],
       pdf='', footer='Chương VII · Màn III — Đêm Trắng Như Vừa Tỉnh Mộng', side=False),
  dict(id='c7-man4', arc='Chương VII · Snezhnaya', src='c7_man4.txt', act='Chương VII · Màn IV',
       title='Khúc An Hồn Cõi Âm', sub='Nhiệm vụ Ma Thần — Snezhnaya',
       hero='nc_snezhnaya_shadow.png',
       cast=[LUMINE, PAIMON,
         dict(name='Anastasya', role="Nữ Hoàng Băng Giá · “Người Mẹ Của Khaenri'ah”", img='anastasya_icon.png', desc="Mở ra phần quá khứ bị chôn vùi về mối liên hệ giữa bà, Khaenri'ah và nỗi thống khổ dẫn đến kế hoạch đối đầu Thiên Lý."),
         dict(name='Pierro', role='Quan Thống Lĩnh Fatui (“Kẻ Hề” · Eftirvit)', desc="Tiết lộ chân dung thời trẻ mang tên Eftirvit từ Khaenri'ah năm xưa và động cơ khởi tạo tổ chức Fatui."),
         dict(name='Arlecchino · Childe · Pulcinella · Sandrone · Pantalone', role='Các Quan Chấp Hành Fatui', img='arlecchino_icon.png', desc='Góp mặt giữa vòng xoáy biến cố từ ga Rankova Zorya tới Cục Khí Tài.'),
         dict(name='Dainsleif', role='“Kiếm Sĩ Hoàng Hôn”', img='dainsleif_icon.png', desc="Tiến bước vào bóng tối cõi âm cùng Lumine để vạch trần bi kịch năm trăm năm trước của Khaenri'ah."),
         dict(name='Danica · Vesna · Valeriy · Mitya · Odette · Vodyanitsa · Alyosha', role='Triều đình Zapolyarny và các đồng minh Snezhnaya', img='vesna_icon.png', desc='Có mặt tại trận tuyến ga Rankova Zorya; Vesna gửi thông điệp cuối qua Dấu Ấn Sự Sống.'),
         dict(name='Lyney · Lynette · Freminet', role='Thành viên Căn Nhà Hơi Ấm', img='lynette_icon.png', desc='Tiếp ứng nhóm Lumine và bảo vệ đồng đội trước mối đe dọa từ Cục Khí Tài.'),
         dict(name='Ronova · Rhinedottir · Asmoday', role='Các Chấp Chính Của Thiên Lý', desc='Ronova (Cái Chết), Rhinedottir / Naberius (Sự Sống) và Asmoday (Không Gian) xuất hiện trong đối chất và hồi ức của Nữ Hoàng Anastasya.'),
         dict(name='Hroptatyr · Mimameith', role="“Hiền Giả” Khaenri'ah & cô giáo (ký ức)", desc="Hiện lên qua ký ức cổ xưa lý giải nguồn gốc tội lỗi và sự sụp đổ của Khaenri'ah."),
       ],
       pdf='', footer='Chương VII · Màn IV — Khúc An Hồn Cõi Âm', side=False),
  dict(id='c7-man5', arc='Chương VII · Snezhnaya', src='c7_man5.txt', act='Chương VII · Màn V',
       title='Thời Khắc Hủy Diệt', sub='Nhiệm vụ Ma Thần — Snezhnaya',
       hero='nc_snezhnaya_wings.png',
       cast=[LUMINE, PAIMON,
         dict(name='Anastasya', role='Nữ Hoàng Băng Giá của Snezhnaya', img='anastasya_icon.png', desc='Triệu tập hội nghị các quốc gia Teyvat tại Cung Điện Zapolyarny để cùng ứng phó thảm họa Hóa Đất Thánh.'),
         dict(name='Pierro · Pantalone · Sandrone · Arlecchino · Childe', role='Ban lãnh đạo Fatui', img='childe_icon.png', desc='Childe phụ trách tiếp đón phái đoàn các nước; Pierro và các Quan Chấp Hành giữ vai trò trụ cột trong chiến dịch phản công.'),
         dict(name='Vesna · Danica · Mitya', role='Tư lệnh Druzhna, hầu gái trưởng & nghiên cứu sinh Mistilteinn', img='vesna_icon.png', desc='Vesna trấn giữ Cảng Belovodye; Mitya điều phối Kế Hoạch Mistilteinn và Danica phục vụ tại cung điện.'),
         dict(name='Alice · Nicole', role='Hai thành viên Hội Ma Nữ', img='nicole_icon.png', desc='Đáp lời mời tới Snezhnaya mở đường vào lãnh địa của Asmoday cùng sinh linh nhỏ Dex.'),
         dict(name='Gương Ánh Sáng', role='Esoptron · Trạm Phản Hồi Thiết Lập Vô Hằng', desc='Tiếp nhận nguyện vọng bảo vệ Teyvat từ Lumine “người chứng kiến”.'),
         dict(name='Venti · Varka · Dahlia · Amber · Klee', role='Phái đoàn Mondstadt', img='venti_icon.png', desc='Phong Thần dẫn dắt đại diện Mondstadt dự hội nghị (Klee thoáng hiện trong hồi ức của Alice).'),
         dict(name='Zhongli · Ningguang · Zibai · Yelan · Xianyun', role='Phái đoàn Liyue', img='zhongli_icon.png', desc='Zhongli hoàn tất thí luyện tại Vực Đá Sâu, còn Ningguang, Zibai và Yelan đại diện Liyue cùng lời truyền âm từ Xianyun.'),
         dict(name='Raiden Shogun · Sangonomiya Kokomi · Kujou Sara · Beidou · Gorou', role='Phái đoàn Inazuma', img='raiden_icon.png', desc='Lôi Thần cùng đại diện Shogunate và Đảo Watatsumi đáp lời hội tụ tại Snezhnaya.'),
         dict(name='Nahida · Tighnari · Cyno', role='Phái đoàn Sumeru', img='nahida_icon.png', desc='Tiểu Vương Kusanali dẫn đầu phái đoàn Sumeru mang trí tuệ Cây Thế Giới góp sức cho đại cuộc.'),
         dict(name='Neuvillette · Sigewinne · Charlotte', role='Phái đoàn Fontaine', img='neuvillette_icon.png', desc='Thủy Long Vương đại diện Fontaine bước lên bàn đàm phán toàn Teyvat.'),
         dict(name='Mavuika · Chasca · Mualani', role='Phái đoàn Natlan', img='mavuika_icon.png', desc='Hỏa Thần cùng hai chiến binh sáu bộ tộc mang ngọn lửa chiến ý tới Zapolyarny.'),
       ],
       pdf='', footer='Chương VII · Màn V — Thời Khắc Hủy Diệt', side=False),
  dict(id='c7-man6', arc='Chương VII · Snezhnaya', src='c7_man6.txt', act='Chương VII · Màn VI',
       title='Ngày Hôm Qua Gửi Từ Bờ Bên Kia', sub='Nhiệm vụ Ma Thần — Snezhnaya',
       hero='nc_snezhnaya_sacred.png',
       cast=[LUMINE, PAIMON,
         dict(name='Anastasya · Pierro · Valeriy · Mitya · Odette · Vodyanitsa · Alyosha', role='Triều đình Snezhnaya & các chiến hữu Snezhnograd', img='anastasya_icon.png', desc='Cùng chung bước trong chương khép lại hành trình qua bảy quốc gia.'),
         dict(name='Tysyatsky Noy', role='Đại công tước fae cổ đại · Chủ nhân Protakropolis', desc='Bậc vương công fae cổ đại đồng hành trong biến cố cuối cùng tại Snezhnaya.'),
         dict(name='Venti · Varka · Jean · Diluc · Kaeya · Amber', role='Những người bạn Mondstadt', img='venti_icon.png', desc='Hòa cùng tiếng vọng cổ xưa từ Sal Vindagnyr trên ngọn gió Long Tích Tuyết Sơn.'),
         dict(name='Alice · Nicole', role='Hội Ma Nữ', img='nicole_icon.png', desc='Tiếp tục dõi theo và hỗ trợ bước ngoặt cuối cùng của hành trình Teyvat.'),
         dict(name='Ningguang · Xilonen', role='Đại diện Liyue và nghệ nhân Natlan', img='ningguang_icon.png', desc='Góp mặt trong bản hòa âm đa quốc gia của đoạn kết.'),
         dict(name='Raiden Shogun · Yae Miko · Kamisato Ayato · Kamisato Ayaka · Thoma · Sangonomiya Kokomi · Kujou Sara · Kujou Kamaji', role='Phái đoàn Inazuma', img='ayato_icon.png', desc='Đón nhận những dư âm từ Lôi Điểu và khép lại kỷ nguyên mới trên Quần Đảo Inazuma.'),
         dict(name='Nahida · Tighnari · Nilou · Naphis và Cyrus · Thoth · Heryshaf', role='Thảo Quốc Sumeru & các cổ thần Deshret', img='nahida_icon.png', desc='Chứng kiến Trạm Cuối Akasha Mới và những mô phỏng mộng cảnh tái hiện Shouki no Kami cùng Trái Tim Ốc Đảo của Apep.'),
         dict(name='Mavuika · Citlali · Kachina · Kinich · Ajaw · Mualani · Chasca · Ifa · Ororon · Iansan · Varesa · Yohualtecuhtin', role='Các chiến binh Natlan & Dạ Thần', img='varesa_icon.png', desc='Quy tụ cùng toàn bộ sáu bộ tộc trước bình minh kỷ nguyên mới tại Đấu Trường Lửa Thánh.'),
         dict(name='Neuvillette · Furina · Ineffa', role='Đại diện Fontaine và Nod-Krai', img='furina_icon.png', desc='Thủy Long Vương tới Inazuma trong khi Furina (cùng ba Tạo Vật Salon) và Ineffa xuất hiện tại Natlan.'),
         dict(name='Gương Ánh Sáng · Nukvah · Aether', role='Đảo Thiên Không & hồi ức người thân', img='aether_icon.png', desc='Hệ thống tính toán tổng hợp tại “Ngai Thần” trên Đảo Thiên Không và mảnh ký ức ngắn của Lumine về Aether.'),
       ],
       pdf='', footer='Chương VII · Màn VI — Ngày Hôm Qua Gửi Từ Bờ Bên Kia', side=False),
]
