#define alpha( i,j ) A[ (j)*ldA + i ]   // map alpha( i,j ) to array A 
#define beta( i,j )  B[ (j)*ldB + i ]   // map beta( i,j )  to array B
#define gamma( i,j ) C[ (j)*ldC + i ]   // map gamma( i,j ) to array C

void MyGer( int m, int n, double *x, int incx, double *y, int incy, double *A, int ldA);

// Outer product gemm loops over
void MyGemm( int m, int n, int k, double *A, int ldA,
	     double *B, int ldB, double *C, int ldC )
{
  for ( int p=0; p<k; p++ )
// C = Acol_p (*) Brow_p + C    (*) = outer prod of vectors
    MyGer( m, n, &alpha(0,p), 1, &beta(p,0), ldB, C, ldC );
}
  
