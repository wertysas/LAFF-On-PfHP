#define alpha( i,j ) A[ (j)*ldA + i ]   // map alpha( i,j ) to array A 
#define beta( i,j )  B[ (j)*ldB + i ]   // map beta( i,j )  to array B
#define gamma( i,j ) C[ (j)*ldC + i ]   // map gamma( i,j ) to array C

void MyGemv( int m, int n, double *A, int ldA, double *x, int incx, double *y, int incy);

void MyGemm( int m, int n, int k,
	     double *A, int ldA,
	     double *B, int ldB,
	     double *C, int ldC )
{
  for ( int j=0; j<n; j++ )
// c_j = A*b_j + c_j
    MyGemv( m, k,  A,  ldA, &B[ldB*j], 1,  &C[ldC*j], 1);
}
  
