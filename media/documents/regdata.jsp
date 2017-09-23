<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page import="java.sql.*,java.util.*" %>
<%@ page import="javax.servlet.*" %>
<%@ page import="javax.servlet.http.*" %>
<%@ include file="register.jsp" %>

<%@ page import="java.io.*"%>
<jsp:forward page="mainpg.html"></jsp:forward>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" ">
<title>REG DATA</title>
</head>
<body>
<% 
try 
{
	 ResultSet rs=null;
  Class.forName("oracle.jdbc.OracleDriver");
  Connection con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","HP","hp123");
  String teamname = request.getParameter("user_name");
  String email = request.getParameter("user_mail");
  String areacode = request.getParameter("user_area");
  String phone = request.getParameter("user_phone");
  String mem1 = request.getParameter("user_mem1");
  String mem1_last = request.getParameter("mem1_last");
  String mem2 = request.getParameter("user_mem2");
  String mem2_last = request.getParameter("mem2_last");
  String mem3 = request.getParameter("user_mem3");
  String mem3_last = request.getParameter("mem3_last");
  String cllg = request.getParameter("user_cllg");
  Statement stat = con.createStatement();
  stat.executeUpdate("insert into REGISTER(TEAM_NAME,EMAIL_ID,AREACODE,CONTACT_NO,MEM1_FIRSTNAME,MEM1_LASTNAME,MEM2_FIRSTNAME,MEM2_LASTNAME,MEM3_FIRSTNAME,MEM3_LASTNAME,COLLEGE) values('"+teamname+"','"+email+"','"+areacode+"','"+phone+"','"+mem1+"','"+mem1_last+"','"+mem2+"','"+mem2_last+"','"+mem3+"','"+mem3_last+"','"+cllg+"')");
  //rs=stat.executeQuery("select * from REGISTER");
 // out.println("Data is successfully inserted!");%>
<iframe src="mainpg.html" scrolling="auto"></iframe>>
<% }catch(ClassNotFoundException e)
{
    out.println(e.getLocalizedMessage());
}
%>


</body>
</html>