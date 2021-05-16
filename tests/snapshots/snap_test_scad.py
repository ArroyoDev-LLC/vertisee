# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_scad_render[vertices0] joint-1"
] = """$fn = 48;
use </tmp/threedframe/dotSCAD/src/hollow_out.scad>


difference(){
\tunion() {
\t\tunion() {
\t\t\tdifference() {
\t\t\t\thull() {
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, 4509059/400000], [0, 1.00000000000000, 0, -4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, -4509059/400000], [0, 1.00000000000000, 0, -4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, -4509059/400000], [0, 1.00000000000000, 0, 4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, 4509059/400000], [0, 1.00000000000000, 0, 4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846040, 0.162019500664581, -0.781909771172249, -1483394921/80000000], [-0.798519385394142, -0.122139467051667, 0.589447827833894, -22178647/160000000], [0, 0.979199485290272, 0.202899896518616, -33845423/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846040, 0.162019500664581, -0.781909771172249, -397668819/80000000], [-0.798519385394143, -0.122139467051667, 0.589447827833894, 2858279327/160000000], [0, 0.979199485290273, 0.202899896518616, -33845423/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846040, 0.162019500664581, -0.781909771172249, -105447479/80000000], [-0.798519385394143, -0.122139467051667, 0.589447827833894, 2417691447/160000000], [0, 0.979199485290273, 0.202899896518616, 54459823/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846039, 0.162019500664581, -0.781909771172250, -1191173581/80000000], [-0.798519385394143, -0.122139467051666, 0.589447827833893, -462766527/160000000], [0, 0.979199485290273, 0.202899896518616, 54459823/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678217, -0.609950855119775, -0.0652774023209210, -228463833/80000000], [-0.613433928728361, 0.785261872093557, 0.0840393200889355, -117598071/8000000], [0, 0.106413094000588, -0.994322006909845, -216054/15625], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678212, -0.609950855119781, -0.0652774023209215, 1195940743/80000000], [-0.613433928728367, 0.785261872093552, 0.0840393200889347, -69576821/80000000], [0, 0.106413094000587, -0.994322006909845, -216054/15625], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678209, -0.609950855119785, -0.0652774023209213, 95823033/80000000], [-0.613433928728371, 0.785261872093549, 0.0840393200889338, 134674071/8000000], [0, 0.106413094000587, -0.994322006909845, -1428543/125000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678220, -0.609950855119772, -0.0652774023209197, -1328581543/80000000], [-0.613433928728358, 0.785261872093560, 0.0840393200889347, 240336821/80000000], [0, 0.106413094000586, -0.994322006909845, -1428543/125000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tmultmatrix(m = [[0.963953445390092, 0.0765532396148244, -0.254820243750466, -67897/37500], [-0.266070958807180, 0.277346161389831, -0.923193019710263, -385763/37500], [0, 0.957715358687956, 0.287717381701556, 61961/15000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "AB", valign = "center");
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t\tdifference() {
\t\t\t\tunion() {
\t\t\t\t\tdifference() {
\t\t\t\t\t\tmultmatrix(m = [[0.0000003817, 0.0000000000, 1.0000000000, 12.7000000000], [1.0000000000, 0.0000000000, -0.0000003817, -0.0000048471], [-0.0000000000, 1.0000000000, 0.0000000000, 0.0000000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\tlinear_extrude(height = 38.1000000000) {
\t\t\t\t\t\t\t\thollow_out(shell_thickness = 3) {
\t\t\t\t\t\t\t\t\tsquare(center = true, size = 23.5460000000);
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t\tmultmatrix(m = [[-1.00000000000000, 0, 0, 127/4], [0, 1.00000000000000, 0, 0], [0, 0, -1.00000000000000, -11773/1000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\ttranslate(v = [0, 3.0000000000, 0]) {
\t\t\t\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\t\t\t\tunion() {
\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "CC", valign = "center");
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\ttranslate(v = [0, -8.4000000000, 0]) {
\t\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "39.48", valign = "center");
\t\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tdifference() {
\t\t\t\t\t\tmultmatrix(m = [[-0.6019687265, 0.1620190698, -0.7819101440, -9.9302588288], [-0.7985196630, -0.1221390251, 0.5894475433, 7.4859837997], [0.0000000000, 0.9791996117, 0.2028992864, 2.5768209374], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\tlinear_extrude(height = 38.1000000000) {
\t\t\t\t\t\t\t\thollow_out(shell_thickness = 3) {
\t\t\t\t\t\t\t\t\tsquare(center = true, size = 23.5460000000);
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t\tmultmatrix(m = [[0.601968784449281, -0.781909967172005, 0.162019708016434, -4583643/200000], [0.798519619388688, 0.589447498920120, -0.122139524594456, 17277/1000], [0, 0.202900096732087, 0.979199443804024, 359403/20000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\ttranslate(v = [0, 3.0000000000, 0]) {
\t\t\t\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\t\t\t\tunion() {
\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "AC", valign = "center");
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\ttranslate(v = [0, -8.4000000000, 0]) {
\t\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "10.27", valign = "center");
\t\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tdifference() {
\t\t\t\t\t\tmultmatrix(m = [[-0.7897472443, -0.6099494574, -0.0652759496, -0.8290045595], [-0.6134323844, 0.7852632424, 0.0840377890, 1.0672799203], [0.0000000000, 0.1064109937, -0.9943222317, -12.6278923424], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\tlinear_extrude(height = 38.1000000000) {
\t\t\t\t\t\t\t\thollow_out(shell_thickness = 3) {
\t\t\t\t\t\t\t\t\tsquare(center = true, size = 23.5460000000);
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t\tmultmatrix(m = [[-0.789745622172531, 0.0652768540181489, -0.609951460846529, -370137/40000], [-0.613434472669512, -0.0840384947159665, 0.785261535506835, 1191309/100000], [0, 0.994322112665392, 0.106412105818052, -606339/20000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\ttranslate(v = [0, 3.0000000000, 0]) {
\t\t\t\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\t\t\t\tunion() {
\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "AA", valign = "center");
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\ttranslate(v = [0, -8.4000000000, 0]) {
\t\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "11.43", valign = "center");
\t\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t}
\t}
\t/* Holes Below*/
\tunion(){
\t\tunion(){
\t\t\tunion(){
\t\t\t\tmultmatrix(m = [[0.0000003817, 0.0000000000, 1.0000000000, 12.7000000000], [1.0000000000, 0.0000000000, -0.0000003817, -0.0000048471], [-0.0000000000, 1.0000000000, 0.0000000000, 0.0000000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tlinear_extrude(height = 48.1000000000) {
\t\t\t\t\t\tsquare(center = true, size = 17.5460000000);
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tmultmatrix(m = [[-0.6019687265, 0.1620190698, -0.7819101440, -9.9302588288], [-0.7985196630, -0.1221390251, 0.5894475433, 7.4859837997], [0.0000000000, 0.9791996117, 0.2028992864, 2.5768209374], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tlinear_extrude(height = 48.1000000000) {
\t\t\t\t\t\tsquare(center = true, size = 17.5460000000);
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tmultmatrix(m = [[-0.7897472443, -0.6099494574, -0.0652759496, -0.8290045595], [-0.6134323844, 0.7852632424, 0.0840377890, 1.0672799203], [0.0000000000, 0.1064109937, -0.9943222317, -12.6278923424], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tlinear_extrude(height = 48.1000000000) {
\t\t\t\t\t\tsquare(center = true, size = 17.5460000000);
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t}
\t} /* End Holes */ 
}"""

snapshots[
    "test_scad_render[vertices1] joint-2"
] = """$fn = 48;
use </tmp/threedframe/dotSCAD/src/hollow_out.scad>


difference(){
\tunion() {
\t\tunion() {
\t\t\tdifference() {
\t\t\t\thull() {
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, 4509059/400000], [0, 1.00000000000000, 0, -4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, -4509059/400000], [0, 1.00000000000000, 0, -4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, -4509059/400000], [0, 1.00000000000000, 0, 4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, 4509059/400000], [0, 1.00000000000000, 0, 4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846040, 0.162019500664581, -0.781909771172249, -1483394921/80000000], [-0.798519385394142, -0.122139467051667, 0.589447827833894, -22178647/160000000], [0, 0.979199485290272, 0.202899896518616, -33845423/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846040, 0.162019500664581, -0.781909771172249, -397668819/80000000], [-0.798519385394143, -0.122139467051667, 0.589447827833894, 2858279327/160000000], [0, 0.979199485290273, 0.202899896518616, -33845423/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846040, 0.162019500664581, -0.781909771172249, -105447479/80000000], [-0.798519385394143, -0.122139467051667, 0.589447827833894, 2417691447/160000000], [0, 0.979199485290273, 0.202899896518616, 54459823/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846039, 0.162019500664581, -0.781909771172250, -1191173581/80000000], [-0.798519385394143, -0.122139467051666, 0.589447827833893, -462766527/160000000], [0, 0.979199485290273, 0.202899896518616, 54459823/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678217, -0.609950855119775, -0.0652774023209210, -228463833/80000000], [-0.613433928728361, 0.785261872093557, 0.0840393200889355, -117598071/8000000], [0, 0.106413094000588, -0.994322006909845, -216054/15625], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678212, -0.609950855119781, -0.0652774023209215, 1195940743/80000000], [-0.613433928728367, 0.785261872093552, 0.0840393200889347, -69576821/80000000], [0, 0.106413094000587, -0.994322006909845, -216054/15625], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678209, -0.609950855119785, -0.0652774023209213, 95823033/80000000], [-0.613433928728371, 0.785261872093549, 0.0840393200889338, 134674071/8000000], [0, 0.106413094000587, -0.994322006909845, -1428543/125000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678220, -0.609950855119772, -0.0652774023209197, -1328581543/80000000], [-0.613433928728358, 0.785261872093560, 0.0840393200889347, 240336821/80000000], [0, 0.106413094000586, -0.994322006909845, -1428543/125000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tmultmatrix(m = [[0.963953445390092, 0.0765532396148244, -0.254820243750466, -67897/37500], [-0.266070958807180, 0.277346161389831, -0.923193019710263, -385763/37500], [0, 0.957715358687956, 0.287717381701556, 61961/15000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "AB", valign = "center");
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t\tdifference() {
\t\t\t\tunion() {
\t\t\t\t\tdifference() {
\t\t\t\t\t\tmultmatrix(m = [[0.0000003817, 0.0000000000, 1.0000000000, 12.7000000000], [1.0000000000, 0.0000000000, -0.0000003817, -0.0000048471], [-0.0000000000, 1.0000000000, 0.0000000000, 0.0000000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\tlinear_extrude(height = 38.1000000000) {
\t\t\t\t\t\t\t\thollow_out(shell_thickness = 3) {
\t\t\t\t\t\t\t\t\tsquare(center = true, size = 23.5460000000);
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t\tmultmatrix(m = [[-1.00000000000000, 0, 0, 127/4], [0, 1.00000000000000, 0, 0], [0, 0, -1.00000000000000, -11773/1000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\ttranslate(v = [0, 3.0000000000, 0]) {
\t\t\t\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\t\t\t\tunion() {
\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "CC", valign = "center");
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\ttranslate(v = [0, -8.4000000000, 0]) {
\t\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "39.48", valign = "center");
\t\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tdifference() {
\t\t\t\t\t\tmultmatrix(m = [[-0.6019687265, 0.1620190698, -0.7819101440, -9.9302588288], [-0.7985196630, -0.1221390251, 0.5894475433, 7.4859837997], [0.0000000000, 0.9791996117, 0.2028992864, 2.5768209374], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\tlinear_extrude(height = 38.1000000000) {
\t\t\t\t\t\t\t\thollow_out(shell_thickness = 3) {
\t\t\t\t\t\t\t\t\tsquare(center = true, size = 23.5460000000);
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t\tmultmatrix(m = [[0.601968784449281, -0.781909967172005, 0.162019708016434, -4583643/200000], [0.798519619388688, 0.589447498920120, -0.122139524594456, 17277/1000], [0, 0.202900096732087, 0.979199443804024, 359403/20000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\ttranslate(v = [0, 3.0000000000, 0]) {
\t\t\t\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\t\t\t\tunion() {
\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "AC", valign = "center");
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\ttranslate(v = [0, -8.4000000000, 0]) {
\t\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "10.27", valign = "center");
\t\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tdifference() {
\t\t\t\t\t\tmultmatrix(m = [[-0.7897472443, -0.6099494574, -0.0652759496, -0.8290045595], [-0.6134323844, 0.7852632424, 0.0840377890, 1.0672799203], [0.0000000000, 0.1064109937, -0.9943222317, -12.6278923424], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\tlinear_extrude(height = 38.1000000000) {
\t\t\t\t\t\t\t\thollow_out(shell_thickness = 3) {
\t\t\t\t\t\t\t\t\tsquare(center = true, size = 23.5460000000);
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t\tmultmatrix(m = [[-0.789745622172531, 0.0652768540181489, -0.609951460846529, -370137/40000], [-0.613434472669512, -0.0840384947159665, 0.785261535506835, 1191309/100000], [0, 0.994322112665392, 0.106412105818052, -606339/20000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\ttranslate(v = [0, 3.0000000000, 0]) {
\t\t\t\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\t\t\t\tunion() {
\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "AA", valign = "center");
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\ttranslate(v = [0, -8.4000000000, 0]) {
\t\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "11.43", valign = "center");
\t\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t}
\t}
\t/* Holes Below*/
\tunion(){
\t\tunion(){
\t\t\tunion(){
\t\t\t\tmultmatrix(m = [[0.0000003817, 0.0000000000, 1.0000000000, 12.7000000000], [1.0000000000, 0.0000000000, -0.0000003817, -0.0000048471], [-0.0000000000, 1.0000000000, 0.0000000000, 0.0000000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tlinear_extrude(height = 48.1000000000) {
\t\t\t\t\t\tsquare(center = true, size = 17.5460000000);
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tmultmatrix(m = [[-0.6019687265, 0.1620190698, -0.7819101440, -9.9302588288], [-0.7985196630, -0.1221390251, 0.5894475433, 7.4859837997], [0.0000000000, 0.9791996117, 0.2028992864, 2.5768209374], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tlinear_extrude(height = 48.1000000000) {
\t\t\t\t\t\tsquare(center = true, size = 17.5460000000);
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tmultmatrix(m = [[-0.7897472443, -0.6099494574, -0.0652759496, -0.8290045595], [-0.6134323844, 0.7852632424, 0.0840377890, 1.0672799203], [0.0000000000, 0.1064109937, -0.9943222317, -12.6278923424], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tlinear_extrude(height = 48.1000000000) {
\t\t\t\t\t\tsquare(center = true, size = 17.5460000000);
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t}
\t} /* End Holes */ 
}"""

snapshots[
    "test_scad_render[vertices2] joint-3"
] = """$fn = 48;
use </tmp/threedframe/dotSCAD/src/hollow_out.scad>


difference(){
\tunion() {
\t\tunion() {
\t\t\tdifference() {
\t\t\t\thull() {
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, 4509059/400000], [0, 1.00000000000000, 0, -4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, -4509059/400000], [0, 1.00000000000000, 0, -4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, -4509059/400000], [0, 1.00000000000000, 0, 4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[0, 0, 1.00000000000000, 127/10], [1.00000000000000, 0, 0, 4509059/400000], [0, 1.00000000000000, 0, 4509059/400000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846040, 0.162019500664581, -0.781909771172249, -1483394921/80000000], [-0.798519385394142, -0.122139467051667, 0.589447827833894, -22178647/160000000], [0, 0.979199485290272, 0.202899896518616, -33845423/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846040, 0.162019500664581, -0.781909771172249, -397668819/80000000], [-0.798519385394143, -0.122139467051667, 0.589447827833894, 2858279327/160000000], [0, 0.979199485290273, 0.202899896518616, -33845423/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846040, 0.162019500664581, -0.781909771172249, -105447479/80000000], [-0.798519385394143, -0.122139467051667, 0.589447827833894, 2417691447/160000000], [0, 0.979199485290273, 0.202899896518616, 54459823/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.601969094846039, 0.162019500664581, -0.781909771172250, -1191173581/80000000], [-0.798519385394143, -0.122139467051666, 0.589447827833893, -462766527/160000000], [0, 0.979199485290273, 0.202899896518616, 54459823/4000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678217, -0.609950855119775, -0.0652774023209210, -228463833/80000000], [-0.613433928728361, 0.785261872093557, 0.0840393200889355, -117598071/8000000], [0, 0.106413094000588, -0.994322006909845, -216054/15625], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678212, -0.609950855119781, -0.0652774023209215, 1195940743/80000000], [-0.613433928728367, 0.785261872093552, 0.0840393200889347, -69576821/80000000], [0, 0.106413094000587, -0.994322006909845, -216054/15625], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678209, -0.609950855119785, -0.0652774023209213, 95823033/80000000], [-0.613433928728371, 0.785261872093549, 0.0840393200889338, 134674071/8000000], [0, 0.106413094000587, -0.994322006909845, -1428543/125000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmultmatrix(m = [[-0.789746044678220, -0.609950855119772, -0.0652774023209197, -1328581543/80000000], [-0.613433928728358, 0.785261872093560, 0.0840393200889347, 240336821/80000000], [0, 0.106413094000586, -0.994322006909845, -1428543/125000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\tcolor(alpha = 1.0000000000, c = "red") {
\t\t\t\t\t\t\tcube(center = true, size = 1);
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tmultmatrix(m = [[0.963953445390092, 0.0765532396148244, -0.254820243750466, -67897/37500], [-0.266070958807180, 0.277346161389831, -0.923193019710263, -385763/37500], [0, 0.957715358687956, 0.287717381701556, 61961/15000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "AB", valign = "center");
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t\tdifference() {
\t\t\t\tunion() {
\t\t\t\t\tdifference() {
\t\t\t\t\t\tmultmatrix(m = [[0.0000003817, 0.0000000000, 1.0000000000, 12.7000000000], [1.0000000000, 0.0000000000, -0.0000003817, -0.0000048471], [-0.0000000000, 1.0000000000, 0.0000000000, 0.0000000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\tlinear_extrude(height = 38.1000000000) {
\t\t\t\t\t\t\t\thollow_out(shell_thickness = 3) {
\t\t\t\t\t\t\t\t\tsquare(center = true, size = 23.5460000000);
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t\tmultmatrix(m = [[-1.00000000000000, 0, 0, 127/4], [0, 1.00000000000000, 0, 0], [0, 0, -1.00000000000000, -11773/1000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\ttranslate(v = [0, 3.0000000000, 0]) {
\t\t\t\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\t\t\t\tunion() {
\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "CC", valign = "center");
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\ttranslate(v = [0, -8.4000000000, 0]) {
\t\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "39.48", valign = "center");
\t\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tdifference() {
\t\t\t\t\t\tmultmatrix(m = [[-0.6019687265, 0.1620190698, -0.7819101440, -9.9302588288], [-0.7985196630, -0.1221390251, 0.5894475433, 7.4859837997], [0.0000000000, 0.9791996117, 0.2028992864, 2.5768209374], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\tlinear_extrude(height = 38.1000000000) {
\t\t\t\t\t\t\t\thollow_out(shell_thickness = 3) {
\t\t\t\t\t\t\t\t\tsquare(center = true, size = 23.5460000000);
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t\tmultmatrix(m = [[0.601968784449281, -0.781909967172005, 0.162019708016434, -4583643/200000], [0.798519619388688, 0.589447498920120, -0.122139524594456, 17277/1000], [0, 0.202900096732087, 0.979199443804024, 359403/20000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\ttranslate(v = [0, 3.0000000000, 0]) {
\t\t\t\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\t\t\t\tunion() {
\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "AC", valign = "center");
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\ttranslate(v = [0, -8.4000000000, 0]) {
\t\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "10.27", valign = "center");
\t\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tdifference() {
\t\t\t\t\t\tmultmatrix(m = [[-0.7897472443, -0.6099494574, -0.0652759496, -0.8290045595], [-0.6134323844, 0.7852632424, 0.0840377890, 1.0672799203], [0.0000000000, 0.1064109937, -0.9943222317, -12.6278923424], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\tlinear_extrude(height = 38.1000000000) {
\t\t\t\t\t\t\t\thollow_out(shell_thickness = 3) {
\t\t\t\t\t\t\t\t\tsquare(center = true, size = 23.5460000000);
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t\tmultmatrix(m = [[-0.789745622172531, 0.0652768540181489, -0.609951460846529, -370137/40000], [-0.613434472669512, -0.0840384947159665, 0.785261535506835, 1191309/100000], [0, 0.994322112665392, 0.106412105818052, -606339/20000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\t\t\ttranslate(v = [0, 3.0000000000, 0]) {
\t\t\t\t\t\t\t\tresize(newsize = [9, 0, 1.5000000000]) {
\t\t\t\t\t\t\t\t\tunion() {
\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "AA", valign = "center");
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\ttranslate(v = [0, -8.4000000000, 0]) {
\t\t\t\t\t\t\t\t\t\t\tlinear_extrude(center = true, height = 1.5000000000) {
\t\t\t\t\t\t\t\t\t\t\t\ttext($fn = 48, direction = "ltr", font = "Impact:style=Bold", halign = "center", size = 6, spacing = 1.2000000000, text = "11.43", valign = "center");
\t\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t\t}
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t}
\t}
\t/* Holes Below*/
\tunion(){
\t\tunion(){
\t\t\tunion(){
\t\t\t\tmultmatrix(m = [[0.0000003817, 0.0000000000, 1.0000000000, 12.7000000000], [1.0000000000, 0.0000000000, -0.0000003817, -0.0000048471], [-0.0000000000, 1.0000000000, 0.0000000000, 0.0000000000], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tlinear_extrude(height = 48.1000000000) {
\t\t\t\t\t\tsquare(center = true, size = 17.5460000000);
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tmultmatrix(m = [[-0.6019687265, 0.1620190698, -0.7819101440, -9.9302588288], [-0.7985196630, -0.1221390251, 0.5894475433, 7.4859837997], [0.0000000000, 0.9791996117, 0.2028992864, 2.5768209374], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tlinear_extrude(height = 48.1000000000) {
\t\t\t\t\t\tsquare(center = true, size = 17.5460000000);
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tmultmatrix(m = [[-0.7897472443, -0.6099494574, -0.0652759496, -0.8290045595], [-0.6134323844, 0.7852632424, 0.0840377890, 1.0672799203], [0.0000000000, 0.1064109937, -0.9943222317, -12.6278923424], [0, 0, 0, 1.0000000000]]) {
\t\t\t\t\tlinear_extrude(height = 48.1000000000) {
\t\t\t\t\t\tsquare(center = true, size = 17.5460000000);
\t\t\t\t\t}
\t\t\t\t}
\t\t\t}
\t\t}
\t} /* End Holes */ 
}"""
